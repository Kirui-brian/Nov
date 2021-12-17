from user import User
from userPost import Post

app_user_one = User("brinkiru@gmail.com", "Kirui Brian", "muren", "Computer Science Student")
app_user_one.get_user_inf0()

app_user_two = User("kamal@gmail.com", "Kamal Muren", "jamalii", "Software Developer")
app_user_two.get_user_inf0()

new_post = Post("On The Daily Mirror today written by", app_user_two.name)
new_post.get_post_info()
