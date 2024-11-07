from database import db  # Importa o SQLAlchemy configurado em database.py

# models.py
from database import db

class CompanyProfile(db.Model):
    __tablename__ = 'company_profiles'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255), nullable=False)
    general_info = db.Column(db.Text)
    brand_voice = db.Column(db.Text)
    brand_description = db.Column(db.Text)
    call_to_action = db.Column(db.Text)
    created_at = db.Column(db.DateTime, default=db.func.current_timestamp())

    campaigns = db.relationship('Campaign', backref='company', cascade="all, delete-orphan")

class Campaign(db.Model):
    __tablename__ = 'campaigns'

    id = db.Column(db.Integer, primary_key=True)
    company_profile_id = db.Column(db.Integer, db.ForeignKey('company_profiles.id'), nullable=False)
    campaign_title = db.Column(db.String(255), nullable=False)
    campaign_description = db.Column(db.Text)
    target_audience = db.Column(db.Text)
    objectives = db.Column(db.Text)
    created_at = db.Column(db.DateTime, default=db.func.current_timestamp())

    content = db.relationship('CampaignContent', backref='campaign', cascade="all, delete-orphan")

class CampaignContent(db.Model):
    __tablename__ = 'campaign_content'

    id = db.Column(db.Integer, primary_key=True)
    campaign_id = db.Column(db.Integer, db.ForeignKey('campaigns.id'), nullable=False)
    content_type = db.Column(db.Enum('text', 'image', 'video'), nullable=False)
    content = db.Column(db.Text)
    created_at = db.Column(db.DateTime, default=db.func.current_timestamp())

class ContentUsageLog(db.Model):
    __tablename__ = 'content_usage_logs'

    id = db.Column(db.Integer, primary_key=True)
    campaign_content_id = db.Column(db.Integer, db.ForeignKey('campaign_content.id'), nullable=False)
    usage_context = db.Column(db.String(255))
    usage_date = db.Column(db.DateTime, default=db.func.current_timestamp())
