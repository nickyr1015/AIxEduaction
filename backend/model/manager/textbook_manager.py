import os
import sys
import pandas as pd
parent_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
sys.path.append(parent_dir)
from entity.textbook import Textbook

class TextbookManager:
    def __init__(self, textbook_db):
        self.textbook_db = textbook_db

    def load_textbook(self):
        """Load the textbooks from the CSV file into a pandas DataFrame."""
        if os.path.exists(self.textbook_db):
            df = pd.read_csv(self.textbook_db)
            if df.empty:
                print("Warning: The CSV file is empty. Returning an empty DataFrame.")
                return pd.DataFrame(columns=['course_id', 'textbook_id', 'title', 'preface', 'table'])
            return df
        else:
            return pd.DataFrame(columns=['course_id', 'textbook_id', 'title', 'preface', 'table'])
        
    def save_textbook(self, df):
        """Save the textbooks DataFrame to the CSV file."""
        df.to_csv(self.textbook_db, index=False)

    def get_textbook_by_id(self, course_id, textbook_id):
        """Get a specific textbook by its course_id and textbook_id."""
        df = self.load_textbook()
        textbook_row = df[(df['course_id'] == course_id) & (df['textbook_id'] == textbook_id)]
        
        if textbook_row.empty:
            return None
        else:
            return Textbook(
                course_id=textbook_row['course_id'].values[0],
                textbook_id=textbook_row['textbook_id'].values[0],
                title=textbook_row['title'].values[0],
                preface=textbook_row['preface'].values[0],
                table= textbook_row['table'].values[0]
            )

    def get_textbook_all_by_course_id(self, course_id):
        """Retrieve all textbooks for a specific course_id as a list of Textbook objects."""
        df = self.load_textbook()
        course_textbooks = df[df['course_id'] == course_id]

        if course_textbooks.empty:
            return []

        textbooks = []
        for _, row in course_textbooks.iterrows():
            textbook = Textbook(
                course_id=row['course_id'],
                textbook_id=row['textbook_id'],
                title=row['title'],
                preface=row['preface'],
                table=row['table']
            )
            textbooks.append(textbook)

        return textbooks

    def get_textbook_all(self):
        """Retrieve all textbooks from the CSV file as a list of dictionaries."""
        df = self.load_textbook()
        textbooks = []

        for _, textbook_row in df.iterrows():
            textbook = Textbook(
                course_id=textbook_row['course_id'],
                textbook_id=textbook_row['textbook_id'],
                title=textbook_row['title'],
                preface=textbook_row['preface'],
                table=textbook_row['table']
            )
            textbooks.append(textbook)

        return textbooks
    
    def get_textbook_id_all_by_course_id(self, course_id):
        """Retrieve all textbook IDs for a specific course_id."""
        df = self.load_textbook()

        course_textbooks = df[df['course_id'] == course_id]

        if course_textbooks.empty:
            print(f"No textbooks found for course ID {course_id}.")
            return []

        textbook_ids = course_textbooks['textbook_id'].tolist()

        return textbook_ids

    def add_textbook(self, textbook):
        """Add a textbook to the DataFrame and save to the CSV file if it does not already exist."""
        df = self.load_textbook()

        if df.empty:
            df = pd.DataFrame(columns=['course_id', 'textbook_id', 'title', 'preface', 'table'])
        
        

        if df[(df['course_id'] == textbook.course_id) & (df['textbook_id'] == textbook.textbook_id)].any().any():
            print(f"Textbook with ID {textbook.textbook_id} already exists for course {textbook.course_id}.")
            return False

        new_textbook_row = pd.DataFrame({
            'course_id': [textbook.course_id],
            'textbook_id': [textbook.textbook_id],
            'title': [textbook.title],
            'preface': [textbook.preface],
            'table': [textbook.table],
        })

        df = pd.concat([df, new_textbook_row], ignore_index=True)

        self.save_textbook(df)
        print(f"Textbook with ID {textbook.textbook_id} added successfully.")
        return True

    def remove_textbook_all_by_course_id(self, course_id):
        """Remove all textbooks for a specific course_id and update the CSV file."""
        df = self.load_textbook()

        if df.empty:
            print(f"No textbooks to remove. The file {self.textbook_db} is empty.")
            return False

        if not df['course_id'].eq(course_id).any():
            print(f"No textbooks found for course ID {course_id}.")
            return False

        df = df[df['course_id'] != course_id]

        self.save_textbook(df)
        print(f"All textbooks for course ID {course_id} have been removed successfully.")
        return True

    def remove_textbook_by_id(self, course_id, textbook_id):
        """Remove a textbook by its course_id and textbook_id and update the CSV file."""
        df = self.load_textbook()

        if df.empty:
            print(f"No textbooks to remove. The file {self.textbook_db} is empty.")
            return False

        if not df[(df['course_id'] == course_id) & (df['textbook_id'] == textbook_id)].any().any():
            print(f"Textbook with ID {textbook_id} does not exist for course {course_id}.")
            return False

        df = df[~((df['course_id'] == course_id) & (df['textbook_id'] == textbook_id))]

        self.save_textbook(df)
        print(f"Textbook with ID {textbook_id} for course {course_id} has been removed successfully.")
        return True
    
    def remove_textbook_all(self):
        """Remove all textbooks from the CSV file."""
        df = self.load_textbook()

        if df.empty:
            print("No textbooks to remove. The file is already empty.")
            return False

        empty_df = pd.DataFrame(columns=['course_id', 'textbook_id', 'title', 'preface', 'table'])
        
        self.save_textbook(empty_df)
        print("All textbooks have been removed successfully.")
        return True
    

    def update_textbook_by_id(self, course_id, textbook_id, new_textbook):
        """Update the details of a specific textbook by course_id and textbook_id."""
        df = self.load_textbook()

        # Check if the textbook exists with the given course_id and textbook_id
        textbook_exists = df[(df['course_id'] == course_id) & (df['textbook_id'] == textbook_id)]

        if textbook_exists.empty:
            print(f"No textbook found for course ID {course_id} and textbook ID {textbook_id}.")
            return False

        # Update the relevant fields
        df.loc[(df['course_id'] == course_id) & (df['textbook_id'] == textbook_id), 'title'] = new_textbook.title
        df.loc[(df['course_id'] == course_id) & (df['textbook_id'] == textbook_id), 'preface'] = new_textbook.preface
        df.loc[(df['course_id'] == course_id) & (df['textbook_id'] == textbook_id), 'table'] = new_textbook.table

        # Save the updated DataFrame back to the CSV
        self.save_textbook(df)
        print(f"Textbook with ID {textbook_id} for course ID {course_id} updated successfully.")
        return True