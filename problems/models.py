from django.db import models

class Problem(models.Model):
    class Meta:
        db_table = 'problems'

    # Define Enums for difficulty
    class Difficulty(models.TextChoices):
        EASY = "EASY", "Easy"
        MEDIUM = "MEDIUM", "Medium"
        HARD = "HARD", "Hard"

    slug = models.CharField(max_length=50, unique=True)
    title = models.CharField(max_length=100, unique=True)
    leetcode_number = models.IntegerField(null=True, unique=True)
    difficulty = models.CharField(max_length=6, choices=Difficulty.choices)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self) -> str:
        return self.title

class Submission(models.Model):
    class Meta:
        db_table = 'submissions'

    problem = models.ForeignKey(
        Problem,
        on_delete=models.CASCADE,
        related_name="submissions"
    )

    input_data = models.JSONField()

    result = models.JSONField()

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)