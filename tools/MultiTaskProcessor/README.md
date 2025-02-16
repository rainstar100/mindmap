# MultiTaskProcessor

This repository contains the MultiTaskProcessor tool, which is designed to handle multiple tasks concurrently.
you only need to supply tasks list and task_handle(how to do task)

## Installation
To install the MultiTaskProcessor tool, you can use pip to install the required dependencies. Open your terminal and navigate to the directory where the `requirements.txt` file is located. Then, run the following command:

```
pip install -r requirements.txt
```

This will install all the necessary packages for the MultiTaskProcessor tool to run properly.

To install the MultiTaskProcessor tool, follow these steps:

    ```
    pip install -r requirements.txt
    ```

## Usage

To use the MultiTaskProcessor tool, follow these steps:

1. create task list and function of task handle
2. creater processor
3. start processor
4. wait for tasks are completed
5. get results


Here's an example usage:

```python
from multitaskprocessor import MultiThreadTaskProcessor as mttp

# Create an instance of the MultiTaskProcessor
task_list=[....]
def task_handle(task):
    pass
processor = mttp(tasK_list ,task_handle)

processor.start()
processor.wait_completion()
processor.get_results()


## Contributing

Contributions to the MultiTaskProcessor tool are welcome! To contribute, please follow these guidelines:

1. Fork the repository.
2. Create a new branch for your feature or bug fix.
3. Make your changes and commit them.
4. Push your changes to your forked repository.
5. Submit a pull request to the main repository.

## License

This project is licensed under the GUN License. See the [LICENSE](LICENSE) file for more information.
