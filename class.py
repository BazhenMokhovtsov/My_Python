from datetime import date, timezone,datetime
#
#
#
# class Car:
#     def move(self):
#         print(f"Car is moving")
#
#     def stop(self):
#         print("Car stopped")
#
# my_car = Car()

class Comment:
    total_comments = 0
    def __init__(self, text, initial_votes_qty =0):
        self.text = text
        self.vote_qty = initial_votes_qty
        Comment.total_comments += 1
        self.create_time = datetime.today().strftime('%a %d. %b %H:%M')

    def upvote(self, qty = 1):
        self.vote_qty += qty

    def reset_vote_qty(self):
        self.vote_qty = 0

    def comment_info(self):
        return f"Comment: {self.text} | Votes: {self.vote_qty} \nCreated at: {self.create_time}"
    @staticmethod
    def merge_comments(first, second):
        return f'{first} {second}'

first_comment = Comment(f'This is a comment')
print(Comment.total_comments)
print(first_comment.comment_info())
first_comment.upvote(100)
print(first_comment.vote_qty)
my_second_comment = Comment("This is a second comment")
print(Comment.total_comments)

merged_comments = Comment.merge_comments("This is a comment", "This is a second comment")

print(merged_comments)

first_comment.upvote()
print(first_comment.vote_qty)




# Chalenge

class Image:
    def __init__(self, resolution, title, extension):
        self.resolution = resolution
        self.title = title
        self.extension = extension

    def resize(self, new_resolution=0):
        self.resolution = new_resolution

    def rename(self, new_title):
        self.title = new_title

    def change_extension(self, new_extension):
        self.extension = new_extension\

    def __str__(self):
        return f"Image have resolution = {self.resolution} | {self.title}.{self.extension}"

# my_image = Image("800x600", "Image1", "jpeg")
#
# print(my_image)
#
# my_image.resize("1920x1080")
#
# my_image.rename("New_Image")
#
# my_image.change_extension("jpg")
#
# print(my_image)




