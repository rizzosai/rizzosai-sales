# 🚀 RizzosAI Sales Site Deployment Guide

## 📋 Repository Information
- **GitHub Repository**: https://github.com/rizzosai/rizzosai-sales
- **Local Path**: `C:\Users\user\OneDrive\Documents\airizzos\backoffice_site\myaistore\python_project\sales.domain.rizzosai.com\SALES_SITE`

## 🌐 Deploy to Render.com

### Step 1: Access Render Dashboard
1. Go to [render.com](https://render.com)
2. Sign in with your GitHub account
3. Click "New +" → "Web Service"

### Step 2: Connect Repository
1. Select "Build and deploy from a Git repository"
2. Connect your GitHub account if not already connected
3. Select the repository: `rizzosai/rizzosai-sales`
4. Click "Connect"

### Step 3: Configure Service
**Basic Settings:**
- **Name**: `rizzosai-sales` (or your preferred name)
- **Region**: Choose closest to your users
- **Branch**: `main`
- **Runtime**: `Python 3`

**Build Settings:**
- **Build Command**: `pip install -r requirements.txt`
- **Start Command**: `gunicorn app:app`

**Environment Variables:**
- `FLASK_ENV`: `production`
- `PORT`: (leave empty - Render will set this automatically)

### Step 4: Deploy
1. Click "Create Web Service"
2. Wait for deployment to complete (usually 2-5 minutes)
3. Your service will be available at: `https://rizzosai-sales.onrender.com`

### Step 5: Custom Domain (Optional)
To use `sales.rizzosai.com`:
1. In your Render service dashboard, go to "Settings"
2. Scroll to "Custom Domains"
3. Add `sales.rizzosai.com`
4. Configure DNS in your domain registrar:
   - Add CNAME record: `sales` → `rizzosai-sales.onrender.com`

## 🔧 Alternative: Deploy to Heroku

### Step 1: Install Heroku CLI
Download from: https://devcenter.heroku.com/articles/heroku-cli

### Step 2: Login and Create App
```bash
heroku login
heroku create rizzosai-sales
```

### Step 3: Deploy
```bash
git push heroku main
```

### Step 4: Set Environment Variables
```bash
heroku config:set FLASK_ENV=production
```

## 🔄 Integration with Back Office

The sales site is configured to integrate with your back office at:
- **Back Office URL**: `https://rizzosai-backend.onrender.com`
- **Webhook Endpoint**: `/webhook/domain-purchase`

### User Flow:
1. **Sales Site** → User fills domain rental form
2. **Webhook** → Data sent to back office
3. **Back Office** → Account created, user redirected
4. **Dashboard** → User accesses their domain management

## 🛠️ Post-Deployment Checklist

### ✅ Test the Complete Flow:
1. Visit your deployed sales site
2. Fill out the domain rental form
3. Verify webhook sends data to back office
4. Confirm user gets redirected to success page
5. Check that user can access back office dashboard

### ✅ Monitor the Integration:
- Check Render logs for any errors
- Test form submissions
- Verify webhook responses
- Ensure success page redirects properly

### ✅ Domain Configuration:
- Configure custom domain if desired
- Set up SSL certificate (automatic on Render)
- Update DNS records if using custom domain

## 📊 Deployment Status

**Current Status**: ✅ Ready for Deployment
- ✅ Code committed to GitHub
- ✅ Repository created: `rizzosai/rizzosai-sales`
- ✅ Deployment files configured (Procfile, requirements.txt, runtime.txt)
- ✅ Webhook integration with back office ready
- ✅ All templates and error pages created

**Next Steps**:
1. Deploy to Render.com using the guide above
2. Test the complete user flow
3. Configure custom domain if desired

## 🚨 Important Notes

- **Back Office Integration**: The sales site sends webhooks to `https://rizzosai-backend.onrender.com/webhook/domain-purchase`
- **Domain Rental Focus**: All messaging emphasizes domain rental and automatic first 5 referrals
- **Fair Commission System**: Promotes the "Next 5" queue system
- **Mobile Responsive**: Works on all devices

## 📞 Support

If you encounter any issues during deployment:
- Check Render deployment logs
- Verify webhook endpoint is responding
- Test form submissions locally first
- Contact admin@rizzosai.com for assistance

---

🎯 **Your domain rental sales site is ready to generate leads and integrate seamlessly with your back office platform!**