from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth import login
from django.contrib.auth.models import User
import json
import logging

logger = logging.getLogger(__name__)

@csrf_exempt
def firebase_auth(request):
    if request.method == 'POST':
        try:
            logger.info('Received Firebase authentication request')
            data = json.loads(request.body)
            logger.debug('Request data: %s', data)

            uid = data.get('uid')
            email = data.get('email')
            display_name = data.get('displayName')
            photo_url = data.get('photoURL')
            provider = data.get('provider')

            if not all([uid, email]):
                logger.error('Missing required fields: uid=%s, email=%s', uid, email)
                return JsonResponse({
                    'success': False,
                    'message': 'Missing required fields'
                }, status=400)

            # Check if user exists
            try:
                user = User.objects.get(username=uid)
                logger.info('Existing user found: %s', user.username)
            except User.DoesNotExist:
                logger.info('Creating new user with uid: %s', uid)
                # Create new user
                user = User.objects.create_user(
                    username=uid,
                    email=email,
                    first_name=display_name or '',
                    password=uid  # Using uid as password since Firebase handles auth
                )

            # Log the user in
            login(request, user)
            logger.info('User %s logged in successfully', user.username)

            return JsonResponse({
                'success': True,
                'message': 'Authentication successful'
            })
        except json.JSONDecodeError as e:
            logger.error('JSON decode error: %s', str(e))
            return JsonResponse({
                'success': False,
                'message': 'Invalid JSON data'
            }, status=400)
        except Exception as e:
            logger.error('Unexpected error: %s', str(e))
            return JsonResponse({
                'success': False,
                'message': str(e)
            }, status=500)
    return JsonResponse({
        'success': False,
        'message': 'Invalid request method'
    }, status=405) 