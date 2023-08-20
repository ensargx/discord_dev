import requests
import config

def upload_github(owner, filename, b64content):
    """
    Upload a file to a GitHub repo.
    All uploaded files are stored in the uploads folder.
    The file is uploaded to the uploads/{owner}/{filename} path.

    Parameters
    ----------
    owner : str
        The owner of the file.
    filename : str
        The name of the file.
    b64content : str
        The base64 encoded content of the file.

    Returns
    -------
    bool
        True if the file is uploaded successfully, False otherwise.
    """
    GITHUB_TOKEN = config.GITHUB_TOKEN
    GITHUB_REPO = config.GITHUB_REPO
    GITHUB_USER = config.GITHUB_USER

    url = f"https://api.github.com/repos/{GITHUB_USER}/{GITHUB_REPO}/contents/uploads/{owner}/{filename}"
    headers = {
        "Accept": "application/vnd.github.v3+json",
        "Authorization": f"token {GITHUB_TOKEN}"
    }
    data = {
        "message": f"Upload from Discord Bot{owner} uploaded {filename}\n\nUploaded by Discord Bot",
        "content": b64content
    }

    r = requests.put(url, headers=headers, json=data)
    if r.status_code == 201:
        return True
    return False
