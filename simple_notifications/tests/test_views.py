from django.urls import reverse_lazy
from test_plus.test import TestCase

from django.contrib.auth import get_user_model

from simple_notifications.factories import UserFactory
from simple_notifications.factories import NotificationFactory
from simple_notifications.factories import GroupFactory

from simple_notifications.models import Notification, UserNotificated



class TestNotificationsUser(TestCase):

    user_factory = UserFactory

    @classmethod
    def setUpTestData(cls):
        user = UserFactory(username="user1")
        NotificationFactory(users=[user])

    def setUp(self):

        User = get_user_model()
        self.user = User.objects.get(username="user1")
        self.notification = Notification.objects.get()

    def test_show_notification(self):
        with self.login(self.user):
            response = self.get('home')
            self.response_200()
            self.assertContext('notification', self.notification)

    def test_count_notification(self):
        with self.login(self.user):
            response = self.post("User_Notificated", pk=self.notification.id)
            self.response_200()
            self.assertJSONEqual(
                str(response.content, encoding='utf8'),
                {"sucess": True}
            )
        user_notificated = UserNotificated.objects.get()
        self.assertEqual(user_notificated.user, self.user)
        self.assertEqual(user_notificated.times_show_to_user, 1)

    def test_no_show_notification(self):
        user_notificated, c = UserNotificated.objects.get_or_create(
            notification=self.notification,
            user=self.user
        )
        user_notificated.times_show_to_user = self.notification.time_to_show
        user_notificated.save()
        with self.login(self.user):
            response = self.get('home')
            self.response_200()
            self.assertEqual("notification" in response.context, False)

    def test_no_show_notification_to_another_user(self):
        user = self.make_user("user2")
        with self.login(user):
            response = self.get('home')
            self.response_200()
            self.assertEqual("notification" in response.context, False)

    def test_user_in_diferent_url_from_notification(self):
        self.notification.url = "/"
        self.notification.save()
        with self.login(self.user):
            response = self.get('test_url')
            self.response_200()
            self.assertEqual("notification" in response.context, False)         


class TestNotificationsGroups(TestCase):
    user_factory = UserFactory

    @classmethod
    def setUpTestData(cls):
        group1 = GroupFactory()
        group2 = GroupFactory()
        user = UserFactory(username="user1")
        user.groups.add(group1)
        user2 = UserFactory(username="user2")
        user2.groups.add(group2)
        NotificationFactory(groups=[group2])

    def setUp(self):
        User = get_user_model()
        self.user = User.objects.get(username="user1")
        self.user2 = User.objects.get(username="user2")
        self.notification = Notification.objects.get()

    def test_show_notification_to_group(self):
        with self.login(self.user2):
            response = self.get('home')
            self.response_200()
            self.assertContext('notification', self.notification)

    def test_no_show_notification_to_another_group(self):
        with self.login(self.user):
            response = self.get('home')
            self.response_200()
            self.assertEqual("notification" in response.context, False)

    def test_notification_for_user_in_group(self):
        with self.login(self.user2):
            response = self.post("User_Notificated", pk=self.notification.id)
            self.response_200()
        self.assertEqual(UserNotificated.objects.count(), 1)
