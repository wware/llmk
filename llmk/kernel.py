from ipykernel.kernelbase import Kernel
import json
import zmq

class LLMKernel(Kernel):
    implementation = 'LLMKernel'
    implementation_version = '1.0'
    language = 'text'
    language_version = '1.0'
    language_info = {
        'name': 'text',
        'mimetype': 'text/plain',
        'file_extension': '.txt'
    }
    banner = "LLM Kernel"

    def do_execute(self, code, silent, 
                  store_history=True, 
                  user_expressions=None, 
                  allow_stdin=False):
        
        if True or not silent:
            # Placeholder response
            response = {
                'status': 'ok',
                'execution_count': self.execution_count,
                'payload': [],
                'user_expressions': {}
            }
            
            self.send_response(self.iopub_socket, 
                'stream', {
                    'name': 'stdout', 
                    'text': f'And we are chatting: {code.strip()}'
                })
            
            return response

if __name__ == '__main__':
    from ipykernel.kernelapp import IPKernelApp
    IPKernelApp.launch_instance(
        kernel_class=LLMKernel)
