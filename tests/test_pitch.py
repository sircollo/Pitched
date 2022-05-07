import unittest
from app.models import Pitch,User
from app import db


class PitchModelTest(unittest.TestCase):
  
    def setUp(self):
      self.user_Collo = User(username = 'Collo', password = 'anything', email = 'collo@gm.com')
      self.new_pitch = Pitch(category = 'Promotion',title='Promotion',pitch='bla bla bla', user= self.user_Collo)
      
      
    def tearDown(self):
      Pitch.query.delete()
      User.query.delete()
      
    def test_instance(self):
        self.assertTrue(isinstance(self.new_pitch, Pitch))

    def test_check_instance_variables(self):
      self.assertEquals(self.new_pitch.category,'Promotion')
      self.assertEquals(self.new_pitch.title,'Promotion')
      self.assertEquals(self.new_pitch.pitch,"bla bla bla")
      self.assertEquals(self.new_pitch.user,self.user_Collo)
      
    def test_save_pitch(self):
      self.new_pitch.save_pitch()
      self.assertTrue(len(Pitch.query.all())>0)
        
   
    def test_get_pitch_by_category(self):
      self.new_pitch.save_pitch()
      found_pitches = Pitch.get_pitches("Promotion")
      self.assertTrue(len(found_pitches) > 0)
