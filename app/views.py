from app import app

from app.blueprints.index.index_bp import index_bp
from app.blueprints.login.login_bp import login_bp
from app.blueprints.browser.browser_bp import browser_bp
from app.blueprints.scan.scan_bp import scan_bp

app.register_blueprint(index_bp)
app.register_blueprint(login_bp, url_prefix="/login")
app.register_blueprint(browser_bp, url_prefix="/browser")
app.register_blueprint(scan_bp, url_prefix="/scan")