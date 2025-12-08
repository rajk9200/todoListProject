from django.shortcuts import render

# Create your views here.
from rest_framework import generics, status
from rest_framework.response import Response
from rest_framework.permissions import AllowAny, IsAuthenticated
from django.contrib.auth import get_user_model
from django.core.mail import send_mail
from django.template.loader import render_to_string
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.utils.encoding import force_bytes, force_str
from django.contrib.auth.tokens import default_token_generator
from django.urls import reverse
from django.conf import settings

from .serializers import (
    UserCreateSerializer,
    MyTokenObtainPairSerializer,
    UserSerializer,
    UserProfileSerializer,
    PasswordResetRequestSerializer,
    PasswordResetConfirmSerializer
)
from rest_framework_simplejwt.views import TokenObtainPairView

User = get_user_model()

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from .serializers import UserDetailSerializer
from rest_framework.parsers import MultiPartParser, FormParser

from .models import Profile
class UserListView(generics.ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserProfileSerializer

class UserListByIDView(APIView):
    def get(self, request, pk=None):
        user = User.objects.filter(pk=pk).first()
        if not user:
            return Response({'detail': 'User not found'}, status=404)
        serializer = UserProfileSerializer(user)
        return Response(serializer.data)

class UserProfileView(APIView):
    permission_classes = [IsAuthenticated]
    parser_classes = [MultiPartParser, FormParser]
    def get(self, request):
        serializer = UserDetailSerializer(request.user)
        return Response(serializer.data)

    def put(self, request):
        serializer = UserDetailSerializer(request.user, data=request.data, partial=True)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)

class RegisterView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserCreateSerializer
    # permission_classes = [AllowAny]


class MyTokenObtainPairView(TokenObtainPairView):
    serializer_class = MyTokenObtainPairSerializer



class PasswordResetRequestView(generics.GenericAPIView):
    serializer_class = PasswordResetRequestSerializer
    # permission_classes = [AllowAny]

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        email = serializer.validated_data['email']
        user = User.objects.filter(email=email).first()

        if user:
            # Generate token and uid
            token = default_token_generator.make_token(user)
            uid = urlsafe_base64_encode(force_bytes(user.pk))

            # Build reset link
            # reset_url = request.build_absolute_uri(
            #     reverse('password-reset-confirm', kwargs={'uidb64': uid, 'token': token})
            # )
            reset_url = f"http://localhost:3000/reset/{uid}/{token}"



            # Send email
            subject = "Password Reset Request"
            message = render_to_string('password_reset_email.html', {
                'user': user,
                'reset_url': reset_url,
            })

            # send_mail(
            #     subject,
            #     message,
            #     settings.DEFAULT_FROM_EMAIL,
            #     [user.email],
            #     fail_silently=False,
            # )
            print(message)

            return Response(
                {'message': f'If this email exists in our system, you will receive a password reset link. {reset_url}'},
                status=status.HTTP_200_OK
            )
        else:
            return Response(
                {'message': 'Email Incorrect.'},
                status=status.HTTP_400_BAD_REQUEST
            )





class PasswordResetConfirmView(generics.GenericAPIView):
    serializer_class = PasswordResetConfirmSerializer
    # permission_classes = [AllowAny]

    def post(self, request, uidb64, token, *args, **kwargs):
        print(request.data)
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        try:
            uid = force_str(urlsafe_base64_decode(uidb64))
            user = User.objects.get(pk=uid)
        except (TypeError, ValueError, OverflowError, User.DoesNotExist):
            user = None

        if user is not None and default_token_generator.check_token(user, token):
            user.set_password(serializer.validated_data['new_password'])
            user.save()
            return Response(
                {'message': 'Password has been reset successfully.'},
                status=status.HTTP_200_OK
            )
        else:
            return Response(
                {'message': f'Invalid reset link.{user}'},
                status=status.HTTP_400_BAD_REQUEST
            )


import google.generativeai as genai
from rest_framework.decorators import api_view
from rest_framework.response import Response

genai.configure(api_key="AIzaSyDsGHmqJLDUnJI5h31FTGFUcn116RamIqQ")

class ChatGemini(APIView):
    def post(self, request, pk=None):
        user_msg = request.data.get("content")
        if user_msg:
            model = genai.GenerativeModel("models/gemini-2.5-flash")
            response="working."
            # response = model.generate_content(user_msg)
            return Response({"reply": response})
            # return Responseonse({"reply": response.text})
        else:
            return Response({"reply": "please ask me question."})


from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from rest_framework.parsers import MultiPartParser, FormParser
import os
import mimetypes

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from rest_framework.parsers import MultiPartParser, FormParser
from .serializers import FileUploadSerializer



from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from rest_framework.parsers import MultiPartParser, FormParser
import os
import mimetypes

# For PDF support (choose one):
# Option 1: Using PyPDF2
try:
    import PyPDF2

    PDF_SUPPORT = True
except ImportError:
    PDF_SUPPORT = False


# Option 2: Using pdfplumber (better text extraction)
# try:
#     import pdfplumber
#     PDF_SUPPORT = True
# except ImportError:
#     PDF_SUPPORT = False

class ReadFileView(APIView):
    """
    API endpoint to read text content from uploaded files.
    Endpoint: POST /api/auth/read-file/
    """
    # permission_classes = [IsAuthenticated]  # Optional: Remove if authentication not needed
    parser_classes = [MultiPartParser, FormParser]

    def post(self, request, *args, **kwargs):
        try:
            # Get the uploaded file
            uploaded_file = request.FILES.get('file')

            if not uploaded_file:
                return Response(
                    {'error': 'No file provided'},
                    status=status.HTTP_400_BAD_REQUEST
                )

            # Validate file type (text files and PDFs)
            valid_extensions = ['.txt', '.csv', '.json', '.html', '.css', '.js',
                                '.jsx', '.py', '.java', '.c', '.cpp', '.md', '.markdown', '.pdf']
            file_name = uploaded_file.name
            file_extension = os.path.splitext(file_name)[1].lower()

            if file_extension not in valid_extensions:
                return Response(
                    {'error': f'Invalid file type. Allowed types: {", ".join(valid_extensions)}'},
                    status=status.HTTP_400_BAD_REQUEST
                )

            # Check if it's a PDF file
            is_pdf = file_extension == '.pdf'

            # Check file size (optional: limit to 5MB)
            max_size = 5 * 1024 * 1024  # 5MB
            if uploaded_file.size > max_size:
                return Response(
                    {'error': 'File size exceeds 5MB limit'},
                    status=status.HTTP_400_BAD_REQUEST
                )

            # Read file content
            try:
                if is_pdf:
                    # Extract text from PDF
                    if not PDF_SUPPORT:
                        return Response(
                            {'error': 'PDF support not available. Please install PyPDF2 or pdfplumber.'},
                            status=status.HTTP_400_BAD_REQUEST
                        )

                    uploaded_file.seek(0)  # Reset file pointer

                    # Option 1: Using PyPDF2
                    try:
                        pdf_reader = PyPDF2.PdfReader(uploaded_file)
                        content = ""
                        for page_num in range(len(pdf_reader.pages)):
                            page = pdf_reader.pages[page_num]
                            content += page.extract_text() + "\n\n"
                    except Exception as e:
                        return Response(
                            {'error': f'Failed to extract text from PDF: {str(e)}'},
                            status=status.HTTP_400_BAD_REQUEST
                        )

                    # Option 2: Using pdfplumber (uncomment if using pdfplumber)
                    # try:
                    #     with pdfplumber.open(uploaded_file) as pdf:
                    #         content = ""
                    #         for page in pdf.pages:
                    #             text = page.extract_text()
                    #             if text:
                    #                 content += text + "\n\n"
                    # except Exception as e:
                    #     return Response(
                    #         {'error': f'Failed to extract text from PDF: {str(e)}'},
                    #         status=status.HTTP_400_BAD_REQUEST
                    #     )

                    if not content.strip():
                        return Response(
                            {'error': 'No text content found in PDF. The PDF might be image-based or encrypted.'},
                            status=status.HTTP_400_BAD_REQUEST
                        )
                else:
                    # Read text file
                    try:
                        # Try to read as text with UTF-8 encoding
                        content = uploaded_file.read().decode('utf-8')
                    except UnicodeDecodeError:
                        try:
                            # Try with latin-1 encoding
                            uploaded_file.seek(0)  # Reset file pointer
                            content = uploaded_file.read().decode('latin-1')
                        except Exception as e:
                            return Response(
                                {'error': f'Failed to read file: {str(e)}'},
                                status=status.HTTP_400_BAD_REQUEST
                            )
            except Exception as e:
                return Response(
                    {'error': f'Error processing file: {str(e)}'},
                    status=status.HTTP_400_BAD_REQUEST
                )

            # Get file metadata
            file_type = mimetypes.guess_type(file_name)[0] or 'text/plain'

            # Return response
            return Response({
                'text': content,
                'filename': file_name,
                'file_type': file_type,
                'file_size': uploaded_file.size,
                'message': 'File read successfully'
            }, status=status.HTTP_200_OK)

        except Exception as e:
            return Response(
                {'error': f'Error processing file: {str(e)}'},
                status=status.HTTP_500_INTERNAL_SERVER_ERROR
            )


class ReadFileView(APIView):
    # permission_classes = [IsAuthenticated]
    parser_classes = [MultiPartParser, FormParser]

    def post(self, request, *args, **kwargs):
        serializer = FileUploadSerializer(data={'file': request.FILES.get('file')})

        if serializer.is_valid():
            uploaded_file = serializer.validated_data['file']

            file_extension = os.path.splitext(uploaded_file.name)[1].lower()
            is_pdf = file_extension == '.pdf'

            try:
                if is_pdf:
                    # Extract text from PDF using PyPDF2 or pdfplumber
                    uploaded_file.seek(0)
                    pdf_reader = PyPDF2.PdfReader(uploaded_file)
                    content = ""
                    for page_num in range(len(pdf_reader.pages)):
                        page = pdf_reader.pages[page_num]
                        content += page.extract_text() + "\n\n"
                else:
                    # Read text file
                    try:
                        content = uploaded_file.read().decode('utf-8')
                    except UnicodeDecodeError:
                        uploaded_file.seek(0)
                        content = uploaded_file.read().decode('latin-1')
            except Exception as e:
                return Response(
                    {'error': f'Error processing file: {str(e)}'},
                    status=status.HTTP_400_BAD_REQUEST
                )

            import mimetypes
            file_type = mimetypes.guess_type(uploaded_file.name)[0] or ('application/pdf' if is_pdf else 'text/plain')

            return Response({
                'text': content,
                'filename': uploaded_file.name,
                'file_type': file_type,
                'file_size': uploaded_file.size
            }, status=status.HTTP_200_OK)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class VideoDownloader(APIView):
    # permission_classes = [IsAuthenticated]
    # parser_classes = [MultiPartParser, FormParser]
    def post(self, request, *args, **kwargs):
        url_path= request.POST.get('url')
        if url_path:
            print(url_path)
            return Response({'message':"downloading completed"}, status.HTTP_200_OK)
        return Response({'message':"Error"},status=status.HTTP_400_BAD_REQUEST)




