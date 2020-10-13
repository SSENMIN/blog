import os.path

from migrate.versioning import api

from config import Config
from flaskr import db

db.create_all()
cfg = Config()
if not os.path.exists(cfg.SQLALCHEMY_MIGRATE_REPO):
    api.create(cfg.SQLALCHEMY_MIGRATE_REPO, 'database repository')
    api.version_control(cfg.SQLALCHEMY_DATABASE_URI, cfg.SQLALCHEMY_MIGRATE_REPO)
else:
    api.version_control(cfg.SQLALCHEMY_DATABASE_URI, cfg.SQLALCHEMY_MIGRATE_REPO,
                        api.version(cfg.SQLALCHEMY_MIGRATE_REPO))
