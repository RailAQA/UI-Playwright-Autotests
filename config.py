from typing_extensions import Self
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
        env_file_encoding='utf-8',
        env_nested_delimiter='.'
        )
    
    app_url: HttpUrl
    headless: bool
    browsers: list[Browser]
    test_user: TestUser
    test_data: TestData
    videos_dir: DirectoryPath
    tracing_path: DirectoryPath
    browser_state_file: FilePath

    @classmethod
    def initialize(cls) -> Self:
        videos_dir = DirectoryPath('./videos')
        tracing_path = DirectoryPath('./tracing')
        browser_state_file = FilePath('browser_state.json')

        videos_dir.mkdir(exist_ok=True)
        tracing_path.mkdir(exist_ok=True)
        browser_state_file.touch(exist_ok=True)

        return Settings(
                        videos_dir=videos_dir, 
                        tracing_path=tracing_path, 
                        browser_state_file=browser_state_file
                        )
    
    def get_base_url(self) -> str:
        return f'{self.app_url}/'

settings = Settings.initialize()