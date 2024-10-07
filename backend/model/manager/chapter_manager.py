import os
import sys
import pandas as pd
parent_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
sys.path.append(parent_dir)
from entity.chapter import Chapter
from util.generate_id import generate_id



class ChapterManager:
    def __init__(self, chapter_db):
        self.chapter_db = chapter_db

    def load_chapter(self):
        """Load chapters from the CSV file into a pandas DataFrame."""
        if os.path.exists(self.chapter_db):
            df = pd.read_csv(self.chapter_db)
            if df.empty:
                print("Warning: The CSV file is empty. Returning an empty DataFrame.")
                return pd.DataFrame(columns=['course_id', 'textbook_id', 'chapter_id', 'number', 'title', 'objective', 'summary'])
            return df
        else:
            return pd.DataFrame(columns=['course_id', 'textbook_id', 'chapter_id', 'number', 'title', 'objective', 'summary'])

    def save_chapter(self, df):
        """Save chapters DataFrame to the CSV file."""
        df.to_csv(self.chapter_db, index=False)

    def get_chapter_all(self):
        """Retrieve all chapters from the CSV file as a list of Chapter objects."""
        df = self.load_chapter()
        chapters = []

        for _, row in df.iterrows():
            chapter = Chapter(
                course_id=row['course_id'],
                textbook_id=row['textbook_id'],
                chapter_id=row['chapter_id'],
                number=row['number'],
                title=row['title'],
                objective=row['objective'],
                summary=row['summary']
            )
            chapters.append(chapter)

        return chapters

    def get_chapter_by_id(self, course_id, textbook_id, chapter_id):
        """Get a specific chapter by course_id, textbook_id, and chapter_id."""
        df = self.load_chapter()
        chapter_row = df[(df['course_id'] == course_id) & (df['textbook_id'] == textbook_id) & (df['chapter_id'] == chapter_id)]

        if chapter_row.empty:
            return None  # Return None if chapter not found
        else:
            return Chapter(
                course_id=chapter_row['course_id'].values[0],
                textbook_id=chapter_row['textbook_id'].values[0],
                chapter_id=chapter_row['chapter_id'].values[0],
                number=chapter_row['number'].values[0],
                title=chapter_row['title'].values[0],
                objective=chapter_row['objective'].values[0],
                summary=chapter_row['summary'].values[0]
            )

    def get_chapter_all_by_course_textbook_id(self, course_id, textbook_id):
        """Retrieve all chapters for a specific course_id and textbook_id."""
        df = self.load_chapter()
        filtered_chapters = df[(df['course_id'] == course_id) & (df['textbook_id'] == textbook_id)]

        if filtered_chapters.empty:
            return []  # Return an empty list if no chapters found

        chapters = []
        for _, row in filtered_chapters.iterrows():
            chapter = Chapter(
                course_id=row['course_id'],
                textbook_id=row['textbook_id'],
                chapter_id=row['chapter_id'],
                number=row['number'],
                title=row['title'],
                objective=row['objective'],
                summary=row['summary']
            )
            chapters.append(chapter)

        return chapters

    def get_chapter_id_all(self):
        """Retrieve all chapter IDs from the CSV file."""
        df = self.load_chapter()

        if df.empty:
            print("Warning: No chapters found. Returning an empty list.")
            return []

        chapter_ids = df['chapter_id'].tolist()
        return chapter_ids

    def add_chapter(self, chapter):
        """Add a Chapter object and save it to the CSV."""
        df = self.load_chapter()

        if df.empty:
            df = pd.DataFrame(columns=['course_id', 'textbook_id', 'chapter_id', 'number', 'title', 'objective', 'summary'])

        # Check if the chapter with the given ID already exists
        if not df[(df['course_id'] == chapter.course_id) & (df['textbook_id'] == chapter.textbook_id) & (df['chapter_id'] == chapter.chapter_id)].empty:
            print(f"Chapter with ID {chapter.chapter_id} already exists.")
            return False

        # Create a new DataFrame row for the new chapter
        new_chapter_row = pd.DataFrame({
            'course_id': [chapter.course_id],
            'textbook_id': [chapter.textbook_id],
            'chapter_id': [chapter.chapter_id],
            'number': [chapter.number],
            'title': [chapter.title],
            'objective': [chapter.objective],
            'summary': [chapter.summary],
        })

        # Append the new chapter to the existing DataFrame
        df = pd.concat([df, new_chapter_row], ignore_index=True)

        # Save the updated DataFrame back to the CSV
        self.save_chapter(df)
        print(f"Chapter with ID {chapter.chapter_id} added successfully.")
        return True

    def update_chapter_by_id(self, course_id, textbook_id, chapter_id, updated_chapter):
        """Update a specific chapter by course_id, textbook_id, and chapter_id."""
        df = self.load_chapter()

        # Check if the chapter exists
        if df[(df['course_id'] == course_id) & (df['textbook_id'] == textbook_id) & (df['chapter_id'] == chapter_id)].empty:
            print(f"No chapter found for course ID {course_id}, textbook ID {textbook_id}, and chapter ID {chapter_id}.")
            return False

        # Update the relevant fields
        df.loc[(df['course_id'] == course_id) & (df['textbook_id'] == textbook_id) & (df['chapter_id'] == chapter_id), 'number'] = updated_chapter.number
        df.loc[(df['course_id'] == course_id) & (df['textbook_id'] == textbook_id) & (df['chapter_id'] == chapter_id), 'title'] = updated_chapter.title
        df.loc[(df['course_id'] == course_id) & (df['textbook_id'] == textbook_id) & (df['chapter_id'] == chapter_id), 'objective'] = updated_chapter.objective
        df.loc[(df['course_id'] == course_id) & (df['textbook_id'] == textbook_id) & (df['chapter_id'] == chapter_id), 'summary'] = updated_chapter.summary

        # Save the updated DataFrame back to the CSV
        self.save_chapter(df)
        print(f"Chapter with ID {chapter_id} for course ID {course_id} and textbook ID {textbook_id} updated successfully.")
        return True

    def remove_chapter_all(self):
        """Remove all chapters from the CSV file."""
        df = self.load_chapter()

        if df.empty:
            print("No chapters to remove. The file is already empty.")
            return False

        # Create an empty DataFrame with the same columns
        empty_df = pd.DataFrame(columns=['course_id', 'textbook_id', 'chapter_id', 'number', 'title', 'objective', 'summary'])
        
        # Save the empty DataFrame back to the CSV file
        self.save_chapter(empty_df)
        print("All chapters have been removed successfully.")
        return True

    def remove_chapter_all_by_course_textbook_id(self, course_id, textbook_id):
        """Remove all chapters by course_id and textbook_id."""
        df = self.load_chapter()

        if df.empty:
            print("No chapters to remove. The file is empty.")
            return False

        # Remove chapters with the given course_id and textbook_id
        df = df[(df['course_id'] != course_id) | (df['textbook_id'] != textbook_id)]

        # Save the updated DataFrame back to the CSV
        self.save_chapter(df)
        print(f"All chapters for course ID {course_id} and textbook ID {textbook_id} have been removed successfully.")
        return True

    def remove_chapter_by_id(self, course_id, textbook_id, chapter_id):
        """Remove a specific chapter by course_id, textbook_id, and chapter_id."""
        df = self.load_chapter()

        if df.empty:
            print("No chapters to remove. The file is empty.")
            return False

        # Check if the chapter with the given ID exists
        if df[(df['course_id'] == course_id) & (df['textbook_id'] == textbook_id) & (df['chapter_id'] == chapter_id)].empty:
            print(f"No chapter found for course ID {course_id}, textbook ID {textbook_id}, and chapter ID {chapter_id}.")
            return False

        # Remove the chapter from the DataFrame
        df = df[(df['course_id'] != course_id) | (df['textbook_id'] != textbook_id) | (df['chapter_id'] != chapter_id)]

        # Save the updated DataFrame back to the CSV
        self.save_chapter(df)
        print(f"Chapter with ID {chapter_id} for course ID {course_id} and textbook ID {textbook_id} has been removed successfully.")
        return True