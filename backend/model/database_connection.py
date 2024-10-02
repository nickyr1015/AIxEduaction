import os
import sys
import pandas as pd
parent_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
sys.path.append(parent_dir)
from config.configuration import get_config
from entity.course import Course
from entity.chapter import Chapter
from entity.section import Section
from entity.textbook import Textbook
from util.generate_id import generate_id


class DatabaseConnection:
    def __init__(self):
        self.base_dir = get_config()["base_dir"] + "/backend/data/database"
        self.course_db = self.base_dir + "/course.csv"
        self.textbook_db = self.base_dir + "/textbook.csv"
        self.chapter_db = self.base_dir + "/chapter.csv"
        self.section_db = self.base_dir + "/section.csv"


    """
    course database manipulation:

    load_course: return dataframe from csv
    save_course(df): save dataframe to csv

    get_course_all()
    get_course_by_id(id): return Course object according to id 
    get_course_id_all(): return a list of course_id

    add_course(course): add a Course object and save
    update_course_by_id(id, Course property): update a Course object by id

    remove_course_all(): 
    remove_course_by_id(id): remove a Course object by id
    
    """

    def load_course(self):
        """Load the courses from the CSV file into a pandas DataFrame."""
        if os.path.exists(self.course_db):
            df = pd.read_csv(self.course_db)
            if df.empty:
                print("Warning: The CSV file is empty. Returning an empty DataFrame.")
                return pd.DataFrame(columns=['course_id', 'title', 'description'])
            return df
        else:
            return pd.DataFrame(columns=['course_id', 'title', 'description'])
        
    def save_course(self, df):
        """Save the courses DataFrame to the CSV file."""
        df.to_csv(self.course_db, index=False)

    def get_course_by_course_id(self, course_id):
        """Get a specific course by its course_id."""
        df = self.load_course()
        course_row = df[df['course_id'] == course_id]
        
        if course_row.empty:
            return None  # Return None if course not found
        else:
            return Course(course_id = course_row['course_id'].values[0],
                          title = course_row['title'].values[0],
                          description = course_row['description'].values[0])
        
    def get_course_all(self):
        """Retrieve all courses from the CSV file as a list of Course objects."""
        df = self.load_course()
        courses = []

        for _, row in df.iterrows():
            course = Course(
                course_id=row['course_id'],
                title=row['title'],
                description=row['description']
            )
            courses.append(course)

        return courses
    
    def get_course_id_all(self):
        """Retrieve all course IDs from the CSV file as a list."""
        df = self.load_course()
        
        if df.empty:
            print("Warning: No courses found. Returning an empty list.")
            return []

        course_ids = df['course_id'].tolist()
        return course_ids
        
        
    def add_course(self, course):
        """Add a course to the DataFrame and save to the CSV file if it does not already exist."""
        df = self.load_course()

        if df.empty:
            df = pd.DataFrame(columns=['course_id', 'title', 'description'])

        if df['course_id'].astype(int).eq(course.course_id).any():
            print(f"Course with ID {course.course_id} already exists.")
            return False

        # Create a new DataFrame for the new course
        new_course_row = pd.DataFrame({
            'course_id': [course.course_id],
            'title': [course.title],
            'description': [course.description],
        })

        # Append the new course to the existing DataFrame
        df = pd.concat([df, new_course_row], ignore_index=True)

        # Save the updated DataFrame back to the CSV
        self.save_course(df)
        print(f"Course with ID {course.course_id} added successfully.")
        return True
    
    def remove_course_by_id(self, course_id):
        """Remove a course by its course_id and update the CSV file."""
        df = self.load_course()

        if df.empty:
            print(f"No courses to remove. The file {self.course_db} is empty.")
            return False

        # Check if the course with the given ID exists
        if not df['course_id'].astype(int).eq(course_id).any():
            print(f"Course with ID {course_id} does not exist.")
            return False

        # Remove the course from the DataFrame
        df = df[df['course_id'] != course_id]

        # Save the updated DataFrame back to the CSV
        self.save_course(df)
        print(f"Course with ID {course_id} has been removed successfully.")
        return True
    
    def update_course_by_id(self, course_id, course):
        """Update a course's title and/or description by its course_id."""
        df = self.load_course()

        # Check if the course exists
        if df['course_id'].astype(int).eq(course_id).any():
            # Update the relevant fields
            df.loc[df['course_id'] == course_id, 'title'] = course.title
            df.loc[df['course_id'] == course_id, 'description'] = course.description
            
            self.save_course(df)
            print(f"Course with ID {course_id} updated successfully.")
            return True
        else:
            print(f"No course with ID {course_id} found.")
            return False

    
    def remove_course_all(self):
        """Remove all courses from the CSV file."""
        df = self.load_course()

        if df.empty:
            print("No courses to remove. The file is already empty.")
            return False

        empty_df = pd.DataFrame(columns=['course_id', 'title', 'description'])
        
        self.save_course(empty_df)
        print("All courses have been removed successfully.")
        return True
    

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


    
    """
    textbook database manipulation:

    load_textbook: return dataframe from csv
    save_textbook(df): save dataframe to csv

    get_textbook_all()
    get_textbook_by_id(course_id, textbook_id): return Textbook object by course_id and textbook_id 
    get_textbook_all_by_course_id(course_id): return all textbooks in a course by course_id
    get_textbook_id_all(): return a list of course_id

    add_textbook(textbook): add a Course object and save
    update_textbook_by_id(course_id, textbook_id): update a Course object by id
    
    remove_textbook_all(): 
    remove_textbook_all_by_course_id(course_id)
    remove_textbook_by_id(course_id, textbook_id): remove a Course object by id
    
    """

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
    

