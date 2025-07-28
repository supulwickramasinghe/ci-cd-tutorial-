import unittest
import sys
import os
from app import create_app, db

app = create_app()


# Add the parent directory to the path so we can import app
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

class TestRoutes(unittest.TestCase):
    
    def setUp(self):
        """Set up test fixtures before each test method."""
        # Import inside setUp to avoid initialization issues
        from app import create_app, db
        
        self.app = create_app('testing')  # Use testing config
        self.app_context = self.app.app_context()
        self.app_context.push()
        self.client = self.app.test_client()
        
        # Store db reference
        self.db = db
        
        # Create all database tables
        db.create_all()
    
    def tearDown(self):
        """Clean up after each test method."""
        self.db.session.remove()
        self.db.drop_all()
        self.app_context.pop()
    
    def test_example_route(self):
        """Test your routes here."""
        response = self.client.get('/')
        # Expect 404 since we don't have a root route defined yet
        # Change this based on your actual routes
        self.assertIn(response.status_code, [200, 404])
    
    def test_api_routes(self):
        """Test API routes if you have them."""
        # Add tests for your actual routes
        pass

if __name__ == '__main__':
    unittest.main()