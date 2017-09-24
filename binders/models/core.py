from datetime import datetime
from flask_appbuilder import Model
from flask_appbuilder.models.mixins import AuditMixin, FileColumn, ImageColumn
from sqlalchemy import Column, Boolean, Integer, Text, DateTime, ForeignKey
from sqlalchemy.orm import relationship


class DocumentationType(Model, AuditMixin):
    id = Column(Integer, primary_key=True)
    name = Column(Text, nullable=False, unique=True)

    def __repr__(self):
        return self.name


class Documentation(Model, AuditMixin):
    id = Column(Integer, primary_key=True)
    name = Column(Text, nullable=False, unique=True)
    is_active = Column(Boolean, default=False)
    created_at = Column(DateTime, default=datetime.utcnow())
    updated_at = Column(DateTime, default=datetime.utcnow())
    doc_gen_script = Column(Text, nullable=False)
    doc_html_location = Column(Text, nullable=False)
    documentation_type_id = Column(Integer, ForeignKey('documentation_type.id'), nullable=False)
    documentation_type = relationship('DocumentationType')
    repository_id = Column(Integer, ForeignKey('repository.id'))

    def __repr__(self):
        return self.name


class RepositoryOwner(Model, AuditMixin):
    id = Column(Integer, primary_key=True)
    name = Column(Text, nullable=False, unique=True)

    def __repr__(self):
        return self.name


class RepositoryLang(Model, AuditMixin):
    id = Column(Integer, primary_key=True)
    name = Column(Text, nullable=False, unique=True)

    def __repr__(self):
        return self.name


class Repository(Model, AuditMixin):
    id = Column(Integer, primary_key=True)
    name = Column(Text, nullable=False, unique=True)
    url = Column(Text, nullable=False, unique=False)
    branch = Column(Text, nullable=False, default='master')
    notes = Column(Text, nullable=True)
    created_at = Column(DateTime, default=datetime.utcnow())
    updated_at = Column(DateTime, default=datetime.utcnow())
    repo_owner_id = Column(Integer, ForeignKey('repository_owner.id'), nullable=False)
    repo_owner = relationship('RepositoryOwner')
    repo_lang_id = Column(Integer, ForeignKey('repository_lang.id'), nullable=False)
    repo_lang = relationship('RepositoryLang')
    documentations = relationship('Documentation')

    def __repr__(self):
        return self.name
