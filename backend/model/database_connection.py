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

    get_course_by_id(id): return Course object according to id 
    add_course(course): add a Course object and save
    remove_course_by_id(id): remove a Course object by id
    update_course_by_id(id, Course property): update a Course object by id
    get_course_all()
    remove_course_all(): 
    get_course_id_all(): return a list of course_id

    -----------------------------------------------------------
    
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

    def get_course_by_id(self, course_id):
        """Get a specific course by its course_id."""
        df = self.load_course()
        course_row = df[df['course_id'] == course_id]
        
        if course_row.empty:
            return None  # Return None if course not found
        else:
            return Course(course_id = course_row['course_id'].values[0],
                          title = course_row['title'].values[0],
                          description = course_row['description'].values[0])
        
    def save_course(self, df):
        """Save the courses DataFrame to the CSV file."""
        df.to_csv(self.course_db, index=False)
        
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
    
    def remove_course_all(self):
        """Remove all courses from the CSV file."""
        df = self.load_course()

        if df.empty:
            print("No courses to remove. The file is already empty.")
            return False

        # Create an empty DataFrame with the same columns
        empty_df = pd.DataFrame(columns=['course_id', 'title', 'description'])
        
        # Save the empty DataFrame back to the CSV file
        self.save_course(empty_df)
        print("All courses have been removed successfully.")
        return True
    
    def get_course_id_all(self):
        """Retrieve all course IDs from the CSV file as a list."""
        df = self.load_course()
        
        if df.empty:
            print("Warning: No courses found. Returning an empty list.")
            return []

        course_ids = df['course_id'].tolist()
        return course_ids


if __name__ == "__main__":
    db_conn = DatabaseConnection()

    db_conn.remove_course_all()

    new_course = Course(course_id=generate_id(), title="Data Structure", description="Introduction to Data Structure")
    db_conn.add_course(new_course)
    new_course = Course(course_id=generate_id(), title="Data Structure", description="Intermediate Data Structure")
    db_conn.add_course(new_course)
    new_course = Course(course_id=generate_id(), title="Data Structure", description="Complex Algorithms")
    db_conn.add_course(new_course)
    new_course = Course(course_id=generate_id(), title="Deep Learning", description="Computer Vision, Natural Language Processing")
    db_conn.add_course(new_course)
    new_course = Course(course_id=generate_id(), title="Machine Learning", description="Unsupervised Learning")
    db_conn.add_course(new_course)

    course = db_conn.get_course_all()
    course = [c.to_dict() for c in course]

    print("Get All Course Information")
    for c in course:
        print(c)

