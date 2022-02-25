import uuid

from django.db import models

# Book
# BookInstance
# Author
# Genre
# Language


class Genre(models.Model):
    name = models.CharField(max_length=200, help_text="Informe um gênero (por exemplo: Ficção Científica.")

    def __str__(self):
        return self.name

    class Meta:
        db_table = 'tb_genres'


class Author(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    date_of_birth = models.DateField(null=True, blank=True)
    date_of_death = models.DateField('Morte', null=True, blank=True)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"

    class Meta:
        db_table = 'tb_authors'
        ordering = ["last_name", "first_name"]


class Language(models.Model):
    name = models.CharField(max_length=200, help_text="Informe o idioa do livro (Inglês, Espanhol, etc)")

    def __str__(self):
        return self.name

    class Meta:
        db_table = 'tb_languages'


class Book(models.Model):
    title = models.CharField(max_length=200)
    author = models.ForeignKey("Author", on_delete=models.SET_NULL, null=True)
    summary = models.TextField(max_length=1000, help_text="Informe uma breve descrição para o livro.")
    isbn = models.CharField(
        'ISBN',
        max_length=13,
        unique=True,
        help_text="Informe os 13 caracteres do ISBN. Clique <a href='https://www.isbn-international.org/content/what-isbn'>Aqui</a> para mais informações."
    )
    genre = models.ManyToManyField("Genre", help_text="Informe um Gênero para o livro.")
    language = models.ForeignKey("Language", on_delete=models.SET_NULL, null=True)

    def display_genre(self):
        return ', '.join([genre.name for genre in self.genre.all()[:3]])

    display_genre.short_description = "Gênero"

    def __str__(self):
        return self.title


class BookInstance(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, help_text="ID único para essa cópia do livro")
    book = models.ForeignKey("Book", on_delete=models.RESTRICT, null=True)
    imprint = models.CharField(max_length=200)
    due_back = models.DateField(null=True, blank=True)

    LOAN_STATUS = (
        ('m', 'Em Manutenção'),
        ('o', 'Em Empréstimo'),
        ('a', 'Disponível'),
        ('r', 'Reservado')
    )

    status = models.CharField(
        max_length=1,
        choices=LOAN_STATUS,
        blank=True,
        default='m',
        help_text="Disponibilidade do Livro"
    )

    def __str__(self):
        return f"{self.id} ({self.book.title})"

    class Meta:
        ordering = ['due_back']
