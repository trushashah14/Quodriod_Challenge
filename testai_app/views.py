from django.http import JsonResponse
from robot.run import run
import json
import os
from django.views.decorators.csrf import csrf_exempt


def create_robot_file(test_title, test_steps):
# Construct the content of the Robot Framework test suite file
    file_content = f"""
*** Settings ***
Library    SeleniumLibrary 

*** Test Cases ***
{test_title}
{'\n'.join(f"    {step}" for step in test_steps)}
"""
    # Write the content to a temporary test suite file
    with open('test_suite.robot', 'w') as file:
        file.write(file_content)


def execute_robot_file(robot_file): 
    # Execute the test suite file and return the result
    return(run(robot_file))

@csrf_exempt
def execute_tests(request):
    if request.method == 'POST':
        try:
            # Parse the JSON payload from the request body
            payload = json.loads(request.body)
            tests = payload.get('tests', [])
            
            # Execute each test case in the payload
            for test in tests:
                title = test.get('title', 'Untitled Test')
                steps = test.get('steps', [])

                # Create a temporary Robot Framework test suite file
                create_robot_file(title, steps)    

                # Call the Execute method to execute test suite file and collect the result      
                result = execute_robot_file('test_suite.robot')

                # Delete the temporary test suite file
                os.remove('test_suite.robot')
                passed = result == 0
            # Return the test execution results as a JSON response    
            return JsonResponse({title : passed}, safe=False)
        except Exception as e:
            # Return an error response if an exception occurs
            return JsonResponse({'error': str(e)}, status=400)
    else:
        # Return an error response for non-POST requests
        return JsonResponse({'error': 'Only POST requests are allowed'}, status=405)



# from django.http import JsonResponse
# from robot.api import TestSuiteBuilder
# import json
# from django.views.decorators.csrf import csrf_exempt


# @csrf_exempt
# def execute_tests(request):
#     if request.method == 'POST':
#         try:
#             payload = json.loads(request.body)
#             tests = payload.get('tests', [])

#             results = []

#             for test in tests:
#                 title = test.get('title', 'Untitled Test')
#                 steps = test.get('steps', [])

#                 # Create a Robot Framework test suite
#                 suite = TestSuiteBuilder().build(*steps)

#                 # Execute the test suite
#                 result = suite.run(output=None, stdout=None)

#                 # Extract results
#                 passed = result.return_code == 0
#                 results.append({title: passed})

#             return JsonResponse({'results': results})
#         except Exception as e:
#             return JsonResponse({'error': str(e)}, status=400)
#     else:
#         return JsonResponse({'error': 'Only POST requests are allowed'}, status=405)
