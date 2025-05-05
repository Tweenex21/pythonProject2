from django.db import models


class DocumentTemplate(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True)
    file = models.FileField(upload_to='path/to/')  # Для .docx, .html и др.
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name


class GeneratedDocument(models.Model):
    template = models.ForeignKey(DocumentTemplate, on_delete=models.CASCADE)
    data = models.JSONField()  # Хранение переменных для подстановки
    output_file = models.FileField(upload_to='generated/')
    created_at = models.DateTimeField(auto_now_add=True)