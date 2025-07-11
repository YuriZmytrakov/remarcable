from django.db import models
from django.utils.text import slugify
from django.core.validators import MinValueValidator
from django.contrib.auth import get_user_model

User = get_user_model()


class Category(models.Model):
    name = models.CharField(
        max_length=100,
        unique=True,
        blank=False,
        db_index=True,
        verbose_name="Category Name",
        error_messages={
            "max_length": "Max 100 characters!",
            "unique": "The entered category already exists!",
            "blank": "Cannot be empty!",
        },
    )
    slug = models.SlugField(max_length=100, unique=True, null=False, editable=False)
    description = models.TextField(blank=True, null=True, help_text="Optional but recommended!")
    created_by = models.ForeignKey(
        User,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name="categories",
        verbose_name="Created by",
    )
    created_at = models.DateTimeField(
        auto_now_add=True, editable=False, verbose_name="Created at"
    )

    class Meta:
        verbose_name = "Category"
        verbose_name_plural = "Categories"
        ordering = ["name"]
        constraints = [
            models.UniqueConstraint(
                fields=["name", "slug"], name="unique_category_name_slug"
            )
        ]

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        super().save(*args, **kwargs)


class Tag(models.Model):
    name = models.CharField(
        max_length=50,
        unique=True,
        db_index=True,
        verbose_name="Tag Name",
        error_messages={
            "max_length": "Max 50 characters!",
            "unique": "The entered tag already exists!",
            "blank": "Cannot be empty!",
        },
    )
    slug = models.SlugField(
        max_length=50, unique=True, db_index=True, null=False, editable=False
    )
    description = models.TextField(blank=True, null=True, help_text="Optional but recommended!")
    created_by = models.ForeignKey(
        User,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name="tags",
        verbose_name="Created by",
    )
    created_at = models.DateTimeField(
        auto_now_add=True, editable=False, verbose_name="Created at"
    )

    class Meta:
        verbose_name = "Tag"
        verbose_name_plural = "Tags"
        ordering = ["name"]

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        super().save(*args, **kwargs)


class Product(models.Model):
    name = models.CharField(
        max_length=200, unique=True, db_index=True, verbose_name="Product Name"
    )
    slug = models.SlugField(
        max_length=200, unique=True, db_index=True, null=False, editable=False
    )
    description = models.TextField(blank=True, null=True, help_text="Optional but recommended!")
    price = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        validators=[MinValueValidator(0.1)],
        verbose_name="Price",
        error_messages={
            "invalid": "Enter a valid price!",
        },
    )
    created_by = models.ForeignKey(
        User,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name="products",
        verbose_name="Created by",
    )
    categories = models.ManyToManyField(Category, related_name="products", blank=True)
    tags = models.ManyToManyField(Tag, related_name="products", blank=True)
    stock = models.IntegerField(
        validators=[MinValueValidator(0)],
        verbose_name="Product Quantity",
        error_messages={
            "invalid": "Enter valid number!",
        },
    )
    created_at = models.DateTimeField(auto_now_add=True, editable=False)

    class Meta:
        ordering = ["name"]
        verbose_name = "Product"
        verbose_name_plural = "Products"
        indexes = [
            models.Index(fields=["id", "slug"]),
            models.Index(fields=["name"]),
        ]
        constraints = [
            models.UniqueConstraint(
                fields=["name", "slug"], name="unique_product_name_slug"
            )
        ]

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        super().save(*args, **kwargs)
