from django.shortcuts import render
from subprocess import Popen, PIPE

def compiler_view(request):
    if request.method == 'POST':
        code = request.POST.get('code', '')
        language = request.POST.get('language', '')
        input_value = request.POST.get('input_value', '')
        result = compile_and_execute(code, language, input_value)
        print(code)
        return render(request, 'compiler.html', {'code': code, 'result': result,'language':language})
    else:
        return render(request, 'compiler.html')

def compile_and_execute(code, language, input_value):
    if language == 'python':
        try:
            process = Popen(['python', '-c', code], stdin=PIPE, stdout=PIPE, stderr=PIPE)
        except:
            process = Popen(['python', '-c', code], stdin=PIPE, stdout=PIPE, stderr=PIPE)
    elif language == 'java':
        process = Popen(['javac', 'HelloWorld.java'], stdin=PIPE, stdout=PIPE, stderr=PIPE)
        process.communicate()
        process = Popen(['java', 'HelloWorld'], stdin=PIPE, stdout=PIPE, stderr=PIPE)
    elif language == 'c':
        with open('myprogram.c', 'w') as c_file:
            c_file.write(code)
        process = Popen(['gcc', 'myprogram.c', '-o', 'myprogram'], stdin=PIPE, stdout=PIPE, stderr=PIPE)
    elif language in ['html', 'tailwind', 'bootstrap']:
        return f"<frame>{code}</frame>"
    elif language == 'js':
        try:
            compiled_output = eval(code)
            return compiled_output
        except Exception as e:
            return f"Error: {str(e)}"
    else:
        return 'Unsupported language'

    stdout, stderr = process.communicate(input=input_value.encode('utf-8'))

    if stderr:
        result = stderr.decode('utf-8')
    else:
        result = stdout.decode('utf-8')

    return result