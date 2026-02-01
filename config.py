from pydantic_settings import BaseSettings
from pydantic import EmailStr, FilePath, HttpUrl, DirectoryPath
from enum import Enum

class Browser(str, Enum):
    WEBKIT = 'webkit'
    CHROMIUM = 'chromium'
    FIREFOX = 'firefox'

class TestUser(BaseSettings):
    email: EmailStr
    username: str
    password: str

class TestData(BaseSettings):
    image_png_file: FilePath

class Settings(BaseSettings):
    app_url: HttpUrl
    headless: bool
    browsers: list[Browser]
    test_user: TestUser
    test_data: TestData
    videos_dir: DirectoryPath
    tracing_path: DirectoryPath
    broser_state_file: FilePath