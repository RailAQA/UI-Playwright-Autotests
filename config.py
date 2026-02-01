from pydantic_settings import BaseSettings, SettingsConfigDict
from pydantic import EmailStr, FilePath, HttpUrl, DirectoryPath, BaseModel
from enum import Enum

class Browser(str, Enum):
    WEBKIT = 'webkit'
    CHROMIUM = 'chromium'
    FIREFOX = 'firefox'

class TestUser(BaseModel):
    email: EmailStr
    username: str
    password: str

class TestData(BaseModel):
    image_png_file: FilePath

class Settings(BaseSettings):
    model_config = SettingsConfigDict(
        env_file='.env', 
        env_file_encoding='UTF-8',
        env_nested_delimiter='.'
        )
    
    app_url: HttpUrl
    headless: bool
    browsers: list[Browser]
    test_user: TestUser
    test_data: TestData
    videos_dir: DirectoryPath
    tracing_path: DirectoryPath
    broser_state_file: FilePath