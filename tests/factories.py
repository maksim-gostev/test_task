import factory
from pytest_factoryboy import register
from django.utils import timezone
from birds.models import Birds
from birds_seen.models import BirdsSeen


@register
class BirdsFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Birds

    name = factory.Sequence(lambda n: 'user{0}'.format(n))
    feather_color = factory.Faker('color')
    picture = None

@register
class BirdsSeenFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = BirdsSeen

    birds = factory.SubFactory(BirdsFactory)
    updated = factory.LazyFunction(timezone.now)
    number_vision_acts = factory.Sequence(lambda n: n)