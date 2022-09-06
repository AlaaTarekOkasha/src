from api.test import (
    mixer, APITestCase,
    Courses, status, reverse,
    settings
)


class TestListCoursesTestCases(APITestCase):
    
    def setUp(self):
        self.url = reverse("api:core:list_courses")

    def test_list_courses(self):
        mixer.blend("core.Courses")
        mixer.blend("core.Courses")
        mixer.blend("core.Courses")
        mixer.blend("core.Courses")

        resp = self.client.get(self.url)

        data = resp.json()

        self.assertEqual(resp.status_code, status.HTTP_200_OK)
        self.assertIsInstance(data, list)
        self.assertEqual(len(data), 4)

    def test_list_courses_with_deleted(self):
        mixer.blend("core.Courses", is_deleted=True)
        mixer.blend("core.Courses")
        mixer.blend("core.Courses")
        mixer.blend("core.Courses")

        resp = self.client.get(self.url)

        data = resp.json()

        self.assertEqual(resp.status_code, status.HTTP_200_OK)
        self.assertIsInstance(data, list)
        self.assertEqual(len(data), 3)
        
    def test_empty_courses(self):
        resp = self.client.get(self.url)

        data = resp.json()

        self.assertEqual(resp.status_code, status.HTTP_200_OK)
        self.assertIsInstance(data, list)
        self.assertEqual(data, [])


class TestListTrainersTestCases(APITestCase):
    def setUp(self):
        self.url = reverse("api:core:list_trainers")

    
    def test_list_trainers(self):
        t = mixer.blend("core.Trainers")
        mixer.blend("core.Courses", trainers=t)

        resp = self.client.get(self.url)


