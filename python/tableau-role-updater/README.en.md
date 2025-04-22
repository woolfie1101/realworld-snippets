# Bulk Update Tableau User Roles Script

This script automates the process of updating user roles in a Tableau Server environment based on specific conditions.

## Features

- Bulk update of user roles that match specific conditions
- Test mode supported (limited to 10 users)
- Preview of users to be updated
- Results saved as CSV files
- Detailed logging provided

## Requirements

- Python 3.10 or higher
- tableauserverclient library
- Install dependencies:
```bash
pip install -r requirements.txt
```

## Configuration

1. Set up your Tableau Server connection info in config.py:
```python
config = {
    'my_env': {
        'server': 'https://your-server-url',
        'username': 'your-username',
        'password': 'your-password'
    }
}
```

## How to Use

### 1. Preview users to be updated (new feature)

You can preview the first 10 users that would be updated in test mode:
```bash
python update_user_roles.py --preview
```
- Detailed info of 10 users will be printed to the log
- A file named `test_users_preview_[datetime].csv` will be generated
- Review before running the actual update

### 2. List all users to be updated

Check the full list of users who meet the criteria:
```bash
python update_user_roles.py
```

### 3. Test mode update

Update only the first 10 users (for testing purposes):
```bash
python update_user_roles.py --update --role Explorer --test
```

### 4. Update all matching users

Run the actual role update for all matching users:
```bash
python update_user_roles.py --update --role Explorer
```

## Available Roles

- Viewer
- Explorer
- ExplorerCanPublish
- Creator

## Log Output

- All operations are logged in `role_check_[datetime].log`
- Updated user lists are saved as CSV files

## Notes

1. Always use the preview option to review affected users before applying changes
2. It’s highly recommended to run in test mode first
3. Role changes cannot be undone, proceed with caution

## Troubleshooting

If you encounter errors:
1. Check the log file for details
2. Verify your Tableau Server credentials and configuration
3. Ensure all required libraries are installed