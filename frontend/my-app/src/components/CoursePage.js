import React, { useEffect, useState } from 'react';

const CoursePage = () => {
  const [courses, setCourses] = useState([]); // State to hold the course data
  const [loading, setLoading] = useState(true); // State to manage loading state
  const [error, setError] = useState(null); // State to manage error messages

  // Fetch courses data from the API when the component mounts
  useEffect(() => {
    const fetchCourses = async () => {
      try {
        const response = await fetch('http://localhost:8000/courses'); // Adjust the URL as necessary
        if (!response.ok) {
          throw new Error('Network response was not ok');
        }
        const data = await response.json();
        setCourses(data); // Set the course data in state
      } catch (err) {
        setError(err.message); // Set error message in state
      } finally {
        setLoading(false); // Set loading to false after fetching
      }
    };

    fetchCourses(); // Call the fetch function
  }, []); // Empty dependency array means this effect runs once on mount

  // Render loading, error, or course list
  if (loading) {
    return <div>Loading courses...</div>;
  }

  if (error) {
    return <div>Error: {error}</div>;
  }

  return (
    <div>
      <h1>Course Page</h1>
      {courses.length > 0 ? (
        <ul>
          {courses.map((course, index) => (
            <li key={index}>{JSON.stringify(course)}</li> // Display each course as a JSON string
          ))}
        </ul>
      ) : (
        <p>No courses available.</p>
      )}
    </div>
  );
};

export default CoursePage;
