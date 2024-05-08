# Importing necessary libraries and modules
import os
from abc import ABC
from dataclasses import dataclass
from typing import (
    Any,
    AsyncGenerator,
    Awaitable,
    Callable,
    List,
    Optional,
    TypedDict,
    Union,
    cast,
)
from urllib.parse import urljoin

# Importing aiohttp for asynchronous HTTP requests
import aiohttp

# Importing Azure Search client and models
from azure.search.documents.aio import SearchClient
from azure.search.documents.models import (
    QueryCaptionResult,
    QueryType,
    VectorizedQuery,
    VectorQuery,
)

# Importing OpenAI's asynchronous API
from openai import AsyncOpenAI

# Importing local modules
from core.authentication import AuthenticationHelper
from text import nonewlines

# Defining a dataclass for a Document
@dataclass
class Document:
    id: Optional[str]  # Unique identifier for the document
    content: Optional[str]  # Content of the document
    embedding: Optional[List[float]]  # Embedding for the document
    image_embedding: Optional[List[float]]  # Image embedding for the document
    category: Optional[str]  # Category of the document
    sourcepage: Optional[str]  # Source page of the document
    sourcefile: Optional[str]  # Source file of the document
    oids: Optional[List[str]]  # List of oids for the document