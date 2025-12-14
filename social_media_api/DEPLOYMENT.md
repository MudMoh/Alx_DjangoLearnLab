# Social Media API Deployment Guide

This guide provides detailed instructions for deploying the Social Media API to production environments.

## Prerequisites

- Python 3.13+
- Git
- Heroku CLI (for Heroku deployment)
- PostgreSQL (recommended for production)

## Environment Setup

1. **Clone the repository**:
   ```bash
   git clone https://github.com/your-username/Alx_DjangoLearnLab.git
   cd Alx_DjangoLearnLab/social_media_api
   ```

2. **Create virtual environment**:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

4. **Set up environment variables**:
   ```bash
   cp .env.example .env
   # Edit .env with your production values
   ```

## Heroku Deployment

### Step 1: Prepare the Application

1. **Install Heroku CLI**:
   ```bash
   # Download from https://devcenter.heroku.com/articles/heroku-cli
   heroku --version
   ```

2. **Login to Heroku**:
   ```bash
   heroku login
   ```

### Step 2: Create Heroku Application

1. **Create new Heroku app**:
   ```bash
   heroku create your-social-media-api
   ```

2. **Add PostgreSQL database**:
   ```bash
   heroku addons:create heroku-postgresql:hobby-dev
   ```

### Step 3: Configure Environment Variables

1. **Set environment variables**:
   ```bash
   heroku config:set SECRET_KEY=your-super-secret-key-here
   heroku config:set DEBUG=False
   heroku config:set ALLOWED_HOSTS=your-social-media-api.herokuapp.com
   ```

2. **Check database URL** (automatically set by Heroku):
   ```bash
   heroku config | grep DATABASE_URL
   ```

### Step 4: Deploy the Application

1. **Commit changes**:
   ```bash
   git add .
   git commit -m "Prepare for production deployment"
   ```

2. **Push to Heroku**:
   ```bash
   git push heroku main
   ```

3. **Run database migrations**:
   ```bash
   heroku run python manage.py migrate
   ```

4. **Create superuser** (optional):
   ```bash
   heroku run python manage.py createsuperuser
   ```

5. **Collect static files**:
   ```bash
   heroku run python manage.py collectstatic --noinput
   ```

### Step 5: Verify Deployment

1. **Open the application**:
   ```bash
   heroku open
   ```

2. **Check logs**:
   ```bash
   heroku logs --tail
   ```

## Alternative Deployment Options

### AWS Elastic Beanstalk

1. **Install EB CLI**:
   ```bash
   pip install awsebcli
   ```

2. **Initialize EB application**:
   ```bash
   eb init
   ```

3. **Create environment**:
   ```bash
   eb create production
   ```

4. **Deploy**:
   ```bash
   eb deploy
   ```

### DigitalOcean App Platform

1. **Connect GitHub repository**
2. **Configure build settings**:
   - Build command: `pip install -r requirements.txt`
   - Run command: `gunicorn social_media_api.wsgi`
3. **Set environment variables**
4. **Deploy**

## Production Configuration

### Security Settings

The application includes production-ready security settings:

- HTTPS redirection
- Secure cookies
- XSS protection
- Content type sniffing protection
- HSTS headers

### Static Files

- WhiteNoise middleware for serving static files
- Compressed and cached static files
- Automatic static file collection

### Database

- PostgreSQL recommended for production
- Automatic database URL detection
- Connection pooling via Django

## Monitoring and Maintenance

### Logging

Logs are available via:
```bash
heroku logs --tail
```

### Scaling

- **Web dynos**: Scale horizontally
- **Database**: Upgrade PostgreSQL plan as needed
- **Caching**: Consider Redis for session/cache storage

### Backups

- Database backups via Heroku addons
- Code versioning via Git
- Static assets via cloud storage (AWS S3, etc.)

## Troubleshooting

### Common Issues

1. **Application Error (H10)**:
   - Check logs: `heroku logs --tail`
   - Verify Procfile syntax
   - Check Python version compatibility

2. **Database Connection Issues**:
   - Verify DATABASE_URL environment variable
   - Check database credentials
   - Ensure database is accessible

3. **Static Files Not Loading**:
   - Run `collectstatic` command
   - Verify WhiteNoise configuration
   - Check STATIC_URL settings

### Performance Optimization

1. **Database queries**: Use `select_related` and `prefetch_related`
2. **Caching**: Implement Redis for caching
3. **CDN**: Use CloudFront or similar for static/media files
4. **Monitoring**: Set up New Relic or similar monitoring

## API Documentation

Once deployed, the API will be available at:
`https://your-app-name.herokuapp.com/api/`

Complete API documentation is available in the README.md file.

## Support

For deployment issues, check:
- Heroku Dev Center: https://devcenter.heroku.com/
- Django deployment docs: https://docs.djangoproject.com/en/stable/howto/deployment/
- Project README.md for API documentation