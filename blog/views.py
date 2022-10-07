import binascii
import requests
from django.contrib.sites.models import Site
from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView
from web3 import Web3, HTTPProvider

from .forms import IPFSTransForm
from .models import IndexInfo, Transaction, IPFS
from .serializers import WalletSerializer, DataSerializer, IPFSDataSerializer


def home(request):
    index = IndexInfo.objects.all()[0]
    current_site = Site.objects.get_current()
    w3 = Web3(HTTPProvider())
    return render(request, 'blog/content.html', context={'domain': current_site.domain,
                                                         'index': index, 'w3': w3})


def hex_to_ascii(hex_str):
    hex_str = hex_str.replace(' ', '').replace('0x', '').replace('\t', '').replace('\n', '')
    ascii_str = binascii.unhexlify(hex_str.encode())
    return ascii_str


def create_text_trans(request):
    index = IndexInfo.objects.all()[0]
    return render(request, 'blog/create_text_trans.html', context={'index': index})


def ipfs_trans(request):
    index = IndexInfo.objects.all()[0]
    data_url = ''
    if request.method == "POST":
        form = IPFSTransForm(request.POST, request.FILES)
        if form.is_valid():
            inst = form.save(commit=False)
            inst.save()
            files = {
                'file': bytes(inst.file.read())
            }
            response = requests.post('https://ipfs.infura.io:5001/api/v0/add', files=files,
                                     auth=('29QAqPI0HxrbfPWaTYotMnpdyho', 'a1d30f9c414e15aa990a140ac924f33b'))
            data_url = 'https://ipfs.io/ipfs/' + response.json().get('Hash')
            IPFS.objects.filter().update(hash_ipfs=response.json().get('Hash'))
    form = IPFSTransForm()
    return render(request, 'blog/ipfs_trans.html', context={'index': index, 'form': form, 'data_url': data_url})


class UpdateHashTransaction(APIView):
    def post(self, request, *args, **kwargs):
        transaction = Transaction.objects.get(id=request.data.get('id'))
        transaction.res_hash = request.data.get('res_hash')
        transaction.data = request.data.get('data')
        transaction.save()
        return Response(transaction.res_hash, transaction, transaction.data)


class CreateUserWalletAddress(APIView):
    def post(self, request, *args, **kwargs):
        serializer = WalletSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)


class Data(APIView):
    def post(self, request, *args, **kwargs):
        serializer = DataSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)


class IPFSData(APIView):
    def post(self, request, *args, **kwargs):
        serializer = IPFSDataSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)
