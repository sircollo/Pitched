import unittest
from app.models import Pitch,User,Comment
from app import db

class CommentsTest(unittest.TestCase):
    '''
    Test Class to test the behaviour of the class
    '''

    def setUp(self):
      self.user_Collo = User(username = 'Collo', password = 'anything', email = 'collo@gm.com')
      self.new_pitch = Pitch(category = 'Promotion',title='Promotion',pitch='bla bla bla', user= self.user_Collo)
      self.new_comment = Comment(comment='wonderful',pitch=self.new_pitch,user= self.user_Collo)
      
    def tearDown(self):
        Pitch.query.delete()
        User.query.delete()
        Comment.query.delete()
        
    def test_check_instance_variables(self):
        self.assertEquals(self.new_comment.comment,'wonderful')
        self.assertEquals(self.new_comment.user,self.user_Collo)
        self.assertEquals(self.new_comment.pitch,self.new_pitch)
        
    def test_save_comment(self):
        self.new_comment.save_comment()
        self.assertTrue(len(Comment.query.all()) > 0)
      