## Getting Started

This folder contains the system with An Age Contrived implementation.

### Prerequisites

- Python 3.9

### Installation

1. Create a virtual python environment
   ```sh
   python -m venv venv
   macos: source venv/bin/activate
   windows: venv/scripts/activate
   ```
2. Install required pip packages
   ```sh
   pip install -r requirements.txt
   ```

<!-- USAGE EXAMPLES -->

## Usage

To run this project, the the command:

```sh
python main.py
```

Add the following arguments for a different configuration

```sh
 --agent-id 1
 --resume-path log/AnAgeContrived/dqn/policy.pth
 --seed 3435
 --training-num 10
 --test-num 1
```

For more information refer to docs/UserGuide
