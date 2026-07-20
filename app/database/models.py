

from sqlalchemy import Column, Integer, String, Text, DateTime
from sqlalchemy.sql import func

from app.database.db import Base


class Interaction(Base):

    __tablename__ = "interactions"

    # Primary Key
    id = Column(
        Integer,
        primary_key=True,
        index=True
    )


    # HCP Details
    hcp_name = Column(
        String(100),
        nullable=False
    )

    interaction_type = Column(
        String(100),
        nullable=False
    )


    # Meeting Details
    date = Column(
        String(50),
        nullable=False
    )

    time = Column(
        String(50),
        nullable=False
    )


    # Interaction Information
    attendees = Column(
        Text,
        nullable=True
    )

    topics = Column(
        Text,
        nullable=True
    )

    materials = Column(
        Text,
        nullable=True
    )

    samples = Column(
        Text,
        nullable=True
    )


    # AI Analysis
    sentiment = Column(
        String(50),
        nullable=True
    )


    # Business Outcome
    outcomes = Column(
        Text,
        nullable=True
    )

    follow_up = Column(
        Text,
        nullable=True
    )


    # Groq/LangGraph Generated Data
    summary = Column(
        Text,
        nullable=True
    )

    next_action = Column(
        Text,
        nullable=True
    )


    # Audit Fields
    created_at = Column(
        DateTime,
        server_default=func.now()
    )

    updated_at = Column(
        DateTime,
        onupdate=func.now()
    )