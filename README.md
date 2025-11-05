# RizzosAI Domain Rental Sales Website

This is the sales website for the RizzosAI domain rental platform. It showcases the domain rental business model with the revolutionary "First 5 Referrals" system and integrates with the back office platform.

## Features

- **Domain Rental Focus**: Clear messaging about renting premium space on RizzosAI.com
- **"First 5 Referrals" System**: Emphasizes automatic referral provision
- **Multiple Rental Tiers**: 5 different domain rental levels from $29-$999/day
- **Webhook Integration**: Seamlessly connects to back office platform
- **Responsive Design**: Mobile-friendly with modern UI/UX
- **Success Flow**: Complete user journey from lead capture to back office access

## File Structure

```
SALES_SITE/
├── app.py                 # Main Flask application
├── requirements.txt       # Python dependencies
├── templates/
│   ├── index.html        # Main sales landing page
│   ├── success.html      # Post-purchase success page
│   ├── 404.html          # 404 error page
│   └── 500.html          # 500 error page
└── README.md             # This file
```

## Domain Rental Tiers

1. **Basic Starter** - $29/day
   - Premium subdomain on RizzosAI.com
   - SSL security & hosting included
   - AI-powered landing pages
   - "Next 5" commission access

2. **Starter Tools** - $97/day
   - Everything in Basic + enhanced features
   - Custom subdomain options
   - Advanced analytics

3. **Professional** - $197/day
   - Premium domain portfolio access
   - Multiple subdomain management
   - VIP support

4. **Empire** - $497/day
   - Premium domain authority
   - Enterprise-level hosting
   - White-label options

5. **Enterprise** - $999/day
   - Full domain ownership rights
   - Unlimited subdomain creation
   - Maximum commission potential

## Integration with Back Office

The sales site integrates with the back office platform through:

- **Webhook Endpoint**: `/domain-purchase` forwards to back office
- **Back Office URL**: `https://rizzosai-backend.onrender.com`
- **User Flow**: Sales → Registration → Success → Back Office Dashboard

## Running Locally

1. Navigate to the SALES_SITE directory:
   ```
   cd "C:\Users\user\OneDrive\Documents\airizzos\backoffice_site\myaistore\python_project\sales.domain.rizzosai.com\SALES_SITE"
   ```

2. Install dependencies:
   ```
   pip install -r requirements.txt
   ```

3. Run the Flask app:
   ```
   python app.py
   ```

4. Access the site at: `http://localhost:5000`

## API Endpoints

- `GET /` - Main sales landing page
- `POST /domain-purchase` - Handle domain purchase form submissions
- `GET /success` - Success page after purchase
- `GET /api/plans` - JSON API for plan information
- `GET /health` - Health check endpoint

## Environment Variables

- `PORT` - Server port (default: 5000)
- `FLASK_ENV` - Environment (development/production)

## Deployment

For production deployment:

1. Use a WSGI server like Gunicorn
2. Set `FLASK_ENV=production`
3. Configure proper domain and SSL
4. Update `BACK_OFFICE_URL` if needed

## Domain Rental Business Model

This sales site promotes the revolutionary domain rental model where customers:

1. **Rent Premium Space**: Get subdomain space on high-authority RizzosAI.com
2. **Receive Infrastructure**: Full hosting, SSL, security, and maintenance included
3. **Get 5 Referrals**: Automatic first 5 referrals provided by the system
4. **Earn Commissions**: Access to fair "Next 5" commission distribution system
5. **Scale Empire**: Use earnings to rent additional domain space

## Contact

- **Support Email**: admin@rizzosai.com
- **Back Office**: https://rizzosai-backend.onrender.com
- **Sales Site**: This application

---

**Note**: This sales site is designed to work in conjunction with the RizzosAI back office platform and emphasizes the domain rental business model with automatic referral provision.