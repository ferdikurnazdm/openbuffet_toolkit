from huggingface_hub import (
    HfApi,
    hf_hub_download,
    upload_file,
    delete_file,
    create_repo,
    list_repo_files,
    HfFolder,
)
from typing import Optional, List
import os


class HuggingfaceHandler:
    """
    A utility class for interacting with Hugging Face Hub repositories.
    
    Supports uploading, downloading, listing, and deleting files from a Hugging Face model repository.
    """

    def __init__(
        self,
        hf_username: str,
        hf_token: str,
        repo_name: str,
        repo_type: str = "model"
    ):
        """
        Initializes the HuggingFaceHelper.

        Args:
            hf_username (str): Hugging Face username or organization name.
            hf_token (str): Access token with write permissions.
            repo_name (str): Name of the Hugging Face repository.
            repo_type (str): Type of the repository (e.g., 'model', 'dataset'). Defaults to 'model'.
        """
        self.hf_username = hf_username
        self.hf_token = hf_token
        self.repo_name = repo_name
        self.repo_type = repo_type
        self.repo_id = f"{hf_username}/{repo_name}"
        self.api = HfApi()

        # Save token for CLI operations
        HfFolder.save_token(hf_token)

    def create_repo_if_not_exist(self, private: bool = True) -> None:
        """
        Creates the Hugging Face repository if it does not exist.

        Args:
            private (bool): Whether the repository should be private. Defaults to True.
        """
        try:
            self.api.repo_info(repo_id=self.repo_id, repo_type=self.repo_type)
        except:
            create_repo(
                repo_id=self.repo_id,
                token=self.hf_token,
                repo_type=self.repo_type,
                private=private,
                exist_ok=True
            )

    def upload_file(self, local_path: str, path_in_repo: Optional[str] = None) -> None:
        """
        Uploads a file to the Hugging Face repository.

        Args:
            local_path (str): Path to the local file to upload.
            path_in_repo (str, optional): Destination path in the repo. Defaults to the filename.
        """
        if not path_in_repo:
            path_in_repo = os.path.basename(local_path)

        upload_file(
            path_or_fileobj=local_path,
            path_in_repo=path_in_repo,
            repo_id=self.repo_id,
            repo_type=self.repo_type,
            token=self.hf_token
        )

    def download_file(self, filename: str, local_dir: str = "./") -> str:
        """
        Downloads a file from the Hugging Face repo.

        Args:
            filename (str): File name in the repo.
            local_dir (str): Local directory to save the file.

        Returns:
            str: Path to the downloaded file.
        """
        return hf_hub_download(
            repo_id=self.repo_id,
            repo_type=self.repo_type,
            filename=filename,
            local_dir=local_dir,
            token=self.hf_token
        )

    def delete_file(self, filename: str) -> None:
        """
        Deletes a file from the repository.

        Args:
            filename (str): File name in the repository to delete.
        """
        delete_file(
            path_in_repo=filename,
            repo_id=self.repo_id,
            repo_type=self.repo_type,
            token=self.hf_token
        )

    def list_files(self) -> List[str]:
        """
        Lists all files in the repository.

        Returns:
            List[str]: List of file names in the repo.
        """
        return list_repo_files(
            repo_id=self.repo_id,
            repo_type=self.repo_type,
            token=self.hf_token
        )
