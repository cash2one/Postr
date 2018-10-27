# from typing import List

from kivy.app import App
from kivy.uix.checkbox import CheckBox
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.label import Label
from kivy.uix.spinner import Spinner
from kivy.uix.tabbedpanel import TabbedPanel
from kivy.uix.tabbedpanel import TabbedPanelHeader
from kivy.uix.textinput import TextInput


class TabbedPanelApp(App):
    @classmethod
    def build(cls) -> TabbedPanel:
        performance_layout = FloatLayout()
        posts_layout = FloatLayout()
        events_layout = FloatLayout()
        update_layout = FloatLayout()
        profile_layout = FloatLayout()

        def spinner() -> Spinner:
            spinner = Spinner(
                # default value
                text='Choose a site:',

                # available values
                values=(
                    'Discord', 'Facebook', 'Instagram', 'Reddit',
                    'Slack', 'Tumblr', 'Twitter', 'YouTube',
                ),

                size_hint=(.15, .1),
                pos=(15, 985),
            )

            def show_selected_value(spinner: Spinner, text: str) -> None:
                print('The spinner', spinner, 'have text', text)

            spinner.bind(text=show_selected_value)
            return spinner

        performance_spinner = spinner()
        performance_layout.add_widget(performance_spinner)
        performance_layout.add_widget(
            Label(
                text='Follower Count: ', font_size='20sp',
                pos=(300, 900), size_hint=(.15, .2),
                color=(0, 0, 0, 1),
            ),
        )
        performance_layout.add_widget(
            Label(
                text='Total Likes: ', font_size='20sp',
                pos=(300, 850), size_hint=(.15, .2),
                color=(0, 0, 0, 1),
            ),
        )

        post_spinner = spinner()
        posts_layout.add_widget(post_spinner)
        posts_layout.add_widget(
            Label(
                text='Scheduled Posts: ', font_size='20sp',
                pos=(315, 900), size_hint=(.15, .2),
                color=(0, 0, 0, 1),
            ),
        )

        events_spinner = spinner()
        events_layout.add_widget(events_spinner)
        events_layout.add_widget(
            Label(
                text='React to: ', font_size='20sp',
                pos=(275, 900), size_hint=(.15, .2),
                color=(0, 0, 0, 1),
            ),
        )
        events_layout.add_widget(
            Label(
                text='Hastag(s)', font_size='12sp',
                pos=(275, 850), size_hint=(.15, .2),
                color=(0, 0, 0, 1),
            ),
        )
        hashtag_checkbox = CheckBox(pos=(450, 850), size_hint=(.15, .2),)
        events_layout.add_widget(hashtag_checkbox)
        events_layout.add_widget(
            Label(
                text='Key word', font_size='12sp',
                pos=(275, 800), size_hint=(.15, .2),
                color=(0, 0, 0, 1),
            ),
        )
        keyword_checkbox = CheckBox(
            pos=(450, 800), size_hint=(.15, .2),
        )
        events_layout.add_widget(
            keyword_checkbox,
        )
        events_layout.add_widget(
            Label(
                text='Mention/Tag', font_size='12sp',
                pos=(275, 750), size_hint=(.15, .2),
                color=(0, 0, 0, 1),
            ),
        )
        mention_tag_checkbox = CheckBox(
            pos=(450, 750), size_hint=(.15, .2),
        )
        events_layout.add_widget(
            mention_tag_checkbox,
        )
        events_layout.add_widget(
            Label(
                text='Like', font_size='12sp',
                pos=(275, 700), size_hint=(.15, .2),
                color=(0, 0, 0, 1),
            ),
        )
        like_checkbox = CheckBox(
            pos=(450, 700), size_hint=(.15, .2),
        )
        events_layout.add_widget(
            like_checkbox,
        )
        events_layout.add_widget(
            Label(
                text='Comment', font_size='12sp',
                pos=(275, 650), size_hint=(.15, .2),
                color=(0, 0, 0, 1),
            ),
        )
        comment_checkbox = CheckBox(
            pos=(450, 650), size_hint=(.15, .2),
        )
        events_layout.add_widget(
            comment_checkbox,
        )
        events_layout.add_widget(
            Label(
                text='Retweet/Repost/Share', font_size='12sp',
                pos=(275, 600), size_hint=(.15, .2),
                color=(0, 0, 0, 1),
            ),
        )
        retweet_repost_share_checkbox = CheckBox(
            pos=(450, 600), size_hint=(.15, .2),
        )
        events_layout.add_widget(
            retweet_repost_share_checkbox,
        )

        update_spinner = spinner()
        update_layout.add_widget(update_spinner)
        update_layout.add_widget(
            Label(
                text='Search for: ', font_size='20sp',
                pos=(275, 950), size_hint=(.15, .2),
                color=(0, 0, 0, 1),
            ),
        )
        search_input = TextInput(
            multiline=False,
            pos=(300, 970), size_hint=(.15, .04),
        )
        update_layout.add_widget(
            search_input,
        )
        update_layout.add_widget(
            Label(
                text='Replace with: ', font_size='20sp',
                pos=(575, 950), size_hint=(.15, .2),
                color=(0, 0, 0, 1),
            ),
        )
        replace_input = TextInput(
            multiline=False,
            pos=(575, 970), size_hint=(.15, .04),
        )
        update_layout.add_widget(
            replace_input,
        )

        profile_layout.add_widget(
            Label(
                text='Username: ', font_size='20sp',
                pos=(45, 970), size_hint=(.15, .2),
                color=(0, 0, 0, 1),
            ),
        )
        profile_layout.add_widget(
            Label(
                text='TEMP USERNAME', font_size='15sp',
                pos=(275, 967), size_hint=(.15, .2),
                color=(0, 0, 0, 1),
            ),
        )
        profile_layout.add_widget(
            Label(
                text='Change Password: ', font_size='20sp',
                pos=(55, 900), size_hint=(.15, .2),
                color=(0, 0, 0, 1),
            ),
        )
        profile_layout.add_widget(
            Label(
                text='Old Password: ', font_size='12sp',
                pos=(50, 850), size_hint=(.15, .2),
                color=(0, 0, 0, 1),
            ),
        )
        old_password_input = TextInput(
            multiline=False,
            pos=(300, 935), size_hint=(.1, .04),
        )
        profile_layout.add_widget(
            old_password_input,
        )
        profile_layout.add_widget(
            Label(
                text='New Password: ', font_size='12sp',
                pos=(50, 795), size_hint=(.15, .2),
                color=(0, 0, 0, 1),
            ),
        )
        new_password_input = TextInput(
            multiline=False,
            pos=(300, 885), size_hint=(.1, .04),
        )
        profile_layout.add_widget(
            new_password_input,
        )
        profile_layout.add_widget(
            Label(
                text='Confirm New Password: ', font_size='12sp',
                pos=(50, 745), size_hint=(.15, .2),
                color=(0, 0, 0, 1),
            ),
        )
        confirm_new_password_input = TextInput(
            multiline=False,
            pos=(300, 835), size_hint=(.1, .04),
        )
        profile_layout.add_widget(
            confirm_new_password_input,
        )

        tb_panel = TabbedPanel()
        tb_panel.do_default_tab = False
        tb_panel.background_color = (1, 1, 1, 1)
        tb_panel.border = [0, 0, 0, 0]
        tb_panel.background_image = 'path/to/background/image'

        # Create Performance tab
        performance_tab = TabbedPanelHeader(text='Performance')
        performance_tab.content = performance_layout
        tb_panel.add_widget(performance_tab)

        # Create Posts tab
        posts_tab = TabbedPanelHeader(text='Posts')
        posts_tab.content = posts_layout
        tb_panel.add_widget(posts_tab)

        # Create Events tab
        events_tab = TabbedPanelHeader(text='Events')
        events_tab.content = events_layout
        tb_panel.add_widget(events_tab)

        # Create Update tab
        update_tab = TabbedPanelHeader(text='Update')
        update_tab.content = update_layout
        tb_panel.add_widget(update_tab)

        # Create Profile tab
        profile_tab = TabbedPanelHeader(text='Profile')
        profile_tab.content = profile_layout
        tb_panel.add_widget(profile_tab)

        return tb_panel

    # def performance(self, platform: str) -> List[int]:
    #     if platform is 'Reddit':
    #         from postr.reddit_postr import Reddit
    #         reddit = Reddit()
    #         follower_count = len(reddit.get_user_followers('')),
    #         # total_likes = reddit.get_user_likes()
    #         total_likes = 0
    #     elif platform is 'Facebook':
    #         from postr.facebook_api import FacebookApi
    #         facebook = FacebookApi()
    #         follower_count = len(facebook.get_user_followers('')),
    #         total_likes = facebook.get_user_likes(),
    #     elif platform is 'Tumblr':
    #         follower_count = 0,
    #         total_likes = 0,
    #     elif platform is 'Instagram':
    #         follower_count = 0,
    #         total_likes = 0,
    #     elif platform is 'Twitter':
    #         from postr.twitter_postr import Twitter
    #         twitter = Twitter()
    #         follower_count = len(twitter.get_user_followers('')),
    #         total_likes = twitter.get_user_likes(),
    #     elif platform is 'Youtube':
    #         follower_count = 0,
    #         total_likes = 0,
    #     elif platform is 'Slack':
    #         follower_count = 0,
    #         total_likes = 0,
    #     elif platform is 'Discord':
    #         follower_count = 0,
    #         total_likes = 0,
    #     else:
    #         follower_count = 0,
    #         total_likes = 0,
    #     stats = List()
    #     stats.append(follower_count)
    #     stats.append(total_likes)
    #     return stats

    # def events(self, platform):
    #     if platform is 'Reddit':
    #
    #     elif platform is 'Facebook':
    #
    #     elif platform is 'Tumblr':
    #
    #     elif platform is 'Instagram':
    #
    #     elif platform is 'Twitter':
    #
    #     elif platform is 'Youtube':
    #
    #     elif platform is 'Slack':
    #
    #     elif platform is 'Discord':
    #
    #     else:

    # def update(self, platform, search, replace):
    #     if platform is 'Reddit':
    #
    #     elif platform is 'Facebook':
    #
    #     elif platform is 'Tumblr':
    #
    #     elif platform is 'Instagram':
    #
    #     elif platform is 'Twitter':
    #
    #     elif platform is 'Youtube':
    #
    #     elif platform is 'Slack':
    #
    #     elif platform is 'Discord':
    #
    #     else:

    # def update_profile(self, new_password):


if __name__ == '__main__':
    TabbedPanelApp().run()
