from flask import Flask, render_template, request, jsonify, redirect, url_for
import requests
import json
from datetime import datetime
import os

app = Flask(__name__)

# Configuration
BACK_OFFICE_URL = "https://rizzosai-backend.onrender.com"
WEBHOOK_ENDPOINT = f"{BACK_OFFICE_URL}/webhook/domain-purchase"

@app.route('/')
def index():
    """Main sales landing page"""
    return render_template('index.html')

@app.route('/domain-purchase', methods=['POST'])
def handle_domain_purchase():
    """Handle domain purchase form submission"""
    try:
        # Get form data
        data = request.get_json() if request.is_json else request.form.to_dict()
        
        # Validate required fields
        required_fields = ['email', 'first_name']
        for field in required_fields:
            if not data.get(field):
                return jsonify({
                    'status': 'error',
                    'message': f'Missing required field: {field}'
                }), 400
        
        # Prepare webhook data
        webhook_data = {
            'email': data.get('email'),
            'first_name': data.get('first_name'),
            'domain_preference': data.get('domain_preference', ''),
            'selected_plan': data.get('selected_plan', 'basic'),
            'amount': data.get('amount', 29),
            'source': 'sales_website',
            'timestamp': datetime.now().isoformat()
        }
        
        # Send webhook to back office
        response = requests.post(
            WEBHOOK_ENDPOINT,
            json=webhook_data,
            headers={'Content-Type': 'application/json'},
            timeout=30
        )
        
        if response.status_code == 200:
            result = response.json()
            return jsonify({
                'status': 'success',
                'message': 'Domain purchase processed successfully',
                'redirect_url': result.get('redirect_url', '/dashboard'),
                'back_office_url': BACK_OFFICE_URL
            })
        else:
            return jsonify({
                'status': 'error',
                'message': 'Failed to process domain purchase'
            }), 500
            
    except requests.exceptions.RequestException as e:
        print(f"Webhook error: {e}")
        return jsonify({
            'status': 'error',
            'message': 'Unable to connect to back office system'
        }), 500
    except Exception as e:
        print(f"General error: {e}")
        return jsonify({
            'status': 'error',
            'message': 'An unexpected error occurred'
        }), 500

@app.route('/plans')
def plans():
    """Domain rental plans page"""
    return render_template('plans.html')

@app.route('/success')
def success():
    """Success page after domain purchase"""
    return render_template('success.html')

@app.route('/about')
def about():
    """About the domain rental system"""
    return render_template('about.html')

@app.route('/api/plans')
def api_plans():
    """API endpoint for plan information"""
    plans_data = {
        'plans': [
            {
                'name': 'basic',
                'title': 'Basic Starter',
                'price': 29,
                'features': [
                    'Premium subdomain on RizzosAI.com',
                    'SSL security & hosting included',
                    'AI-powered landing pages',
                    '"Next 5" commission access',
                    'Domain management tools',
                    'Basic traffic analytics'
                ]
            },
            {
                'name': 'starter',
                'title': 'Starter Tools',
                'price': 97,
                'features': [
                    'Everything in Basic Starter',
                    'Enhanced domain features',
                    'Custom subdomain options',
                    'Advanced traffic analytics',
                    'Priority domain support',
                    'Multiple page templates'
                ]
            },
            {
                'name': 'professional',
                'title': 'Professional',
                'price': 197,
                'features': [
                    'Everything in Starter Tools',
                    'Premium domain portfolio access',
                    'Multiple subdomain management',
                    'Advanced hosting features',
                    'VIP domain support',
                    'Professional SEO tools'
                ]
            },
            {
                'name': 'empire',
                'title': 'Empire',
                'price': 497,
                'features': [
                    'Everything in Professional',
                    'Premium domain authority',
                    'Custom domain integration',
                    'Enterprise-level hosting',
                    'Dedicated server resources',
                    'White-label options'
                ]
            },
            {
                'name': 'enterprise',
                'title': 'Enterprise',
                'price': 999,
                'features': [
                    'Everything in Empire',
                    'Full domain ownership rights',
                    'White-label domain options',
                    'Unlimited subdomain creation',
                    'Your own domain empire',
                    'Maximum commission potential'
                ]
            }
        ]
    }
    return jsonify(plans_data)

@app.route('/health')
def health_check():
    """Health check endpoint"""
    return jsonify({
        'status': 'healthy',
        'timestamp': datetime.now().isoformat(),
        'service': 'RizzosAI Sales Website'
    })

@app.errorhandler(404)
def not_found(error):
    """404 error handler"""
    return render_template('404.html'), 404

@app.errorhandler(500)
def internal_error(error):
    """500 error handler"""
    return render_template('500.html'), 500

if __name__ == '__main__':
    # Get port from environment variable or default to 5000
    port = int(os.environ.get('PORT', 5000))
    
    # Run the app
    app.run(
        host='0.0.0.0',
        port=port,
        debug=True if os.environ.get('FLASK_ENV') == 'development' else False
    )