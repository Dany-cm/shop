from io import BytesIO

from django.core.files import File
from django.db import models
from PIL import Image


# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=150)
    slug = models.SlugField()

    class Meta:
        ordering = ("name",)
        verbose_name_plural = "Categories"

    def __str__(self):
        return self.name


class Products(models.Model):
    MTG_RARE_CHOICES = (
        ("C", "Common"),
        ("U", "Uncommon"),
        ("R", "Rare"),
        ("M", "Mythic Rare"),
        ("L", "Land"),
    )

    category = models.ForeignKey(
        Category, related_name="products", on_delete=models.CASCADE
    )
    name = models.CharField(max_length=150)
    slug = models.SlugField()
    description = models.TextField(blank=True, null=True)
    edition = models.CharField(max_length=150, blank=True, null=True)
    rarity = models.CharField(max_length=20, choices=MTG_RARE_CHOICES, default="C")
    price = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    image = models.ImageField(upload_to="cartes/", blank=True, null=True)
    thumbnail = models.ImageField(upload_to="thumbnail/", blank=True)

    class Meta:
        ordering = ("-created_at",)
        verbose_name_plural = "Products"

    def __str__(self):
        return self.name

    def get_display_price(self):
        return self.price / 100

    def get_thumbnail(self):
        if self.thumbnail:
            return self.thumbnail.url
        else:
            if self.image:
                self.thumbnail = self.make_thumbnail(self.image)
                self.save()

                return self.thumbnail.url
            else:
                return "/static/images/preview.png"

    def make_thumbnail(self, image, size=(240, 240)):
        img = Image.open(image)
        img.convert("RGB")
        img.thumbnail(size)

        thumb_io = BytesIO()
        img.save(thumb_io, "JPG", quality=63)

        thumbnail = File(thumb_io, name=image.name)
        return thumbnail
