from rest_framework.decorators import api_view
from rest_framework.response import Response

from .models import Entry, Sentence
from .serializers import EntrySerializer
from . import transcriber


@api_view()
def query(request, *args, **kwargs):
    q = request.GET.get('q', '')

    entries = Entry.objects \
            .filter(content__icontains=q) \
            .order_by('content') \
            [:10]

    serializer = EntrySerializer(instance=entries, many=True)

    return Response(data=serializer.data)


@api_view()
def transcribe(request, *args, **kwargs):
    content = request.GET.get('content', '')

    output = transcriber.transcribe(content)

    return Response(data={
        'content': content,
        'output': output
    })


@api_view()
def random_sentence(request, *args, **kwargs):
    sentence = Sentence.objects.order_by('?').first()

    transcribed = transcriber.transcribe(sentence.content)

    return Response(data={
        'content': sentence.content,
        'output': transcribed
    })
