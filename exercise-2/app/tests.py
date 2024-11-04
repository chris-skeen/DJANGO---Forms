from django.test import SimpleTestCase
from app import views

# Create your tests here.

class TestStudent(SimpleTestCase):

  def test_warmup_2(self):
    response = self.client.get('/warmup-2/front-times?string=Chocolate&number=2')
    self.assertContains(response, "ChoCho")

  def test_warmup_2_v2(self):
    response = self.client.get('/warmup-2/front-times?string=Chocolate&number=3')
    self.assertContains(response, "ChoChoCho")

  def test_warmup_2_v3(self):
    response = self.client.get('/warmup-2/front-times?string=Abc&number=2')
    self.assertContains(response, "AbcAbc")

# ------------------------------------------------------------------------------------------------------------------------
  
  def test_logic_2(self):
    response = self.client.get('/logic-2/no-teen-sum?a=1&b=2&c=3')
    self.assertContains(response, 6)

  def test_logic_2_v2(self):
    response = self.client.get('/logic-2/no-teen-sum?a=2&b=13&c=1')
    self.assertContains(response, 3)

  def test_logic_2_v3(self):
    response = self.client.get('/logic-2/no-teen-sum?a=2&b=1&c=15')
    self.assertContains(response, 18)

# ------------------------------------------------------------------------------------------------------------------------

  def test_string_2(self):
    response = self.client.get('/string-2/xyz_there?string=abcxyz')
    self.assertContains(response, True)

  def test_string_2_v2(self):
    response = self.client.get('/string-2/xyz_there?string=abc.xyz')
    self.assertContains(response, False)

  def test_string_2_v3(self):
    response = self.client.get('/string-2/xyz_there?string=xyz.abc')
    self.assertContains(response, True)

# ------------------------------------------------------------------------------------------------------------------------


  def test_list_2(self):
    response = self.client.get('/list-2/centered-average?n1=1&n2=2&n3=3&n4=4&n5=100&n6=&n7=')
    self.assertContains(response, 3)


  def test_list_2_v2(self):
    response = self.client.get('/list-2/centered-average?n1=1&n2=2&n3=3&n4=4&n5=100&n6=&n7=')
    self.assertContains(response, 3)

  def test_list_2_v2(self):
    response = self.client.get('/list-2/centered-average?n1=1&n2=1&n3=5&n4=5&n5=10&n6=8&n7=7')
    self.assertContains(response, 5.2)