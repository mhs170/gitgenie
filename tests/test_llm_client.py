import pytest
from unittest.mock import patch, MagicMock
from gitgenie.llm_client import generate_text


class TestGenerateText:
    """Test suite for generate_text function."""

    @patch('gitgenie.llm_client.ollama.chat')
    def test_generate_text_success(self, mock_chat):
        """Test that generate_text returns content on successful response."""
        # Mock the ollama.chat response
        mock_chat.return_value = {
            'message': {
                'content': 'This is the generated response'
            }
        }
        
        result = generate_text('Test prompt')
        
        assert result == 'This is the generated response'
        mock_chat.assert_called_once_with(
            model='llama3',
            messages=[{'role': 'user', 'content': 'Test prompt'}]
        )

    @patch('gitgenie.llm_client.ollama.chat')
    def test_generate_text_with_different_prompts(self, mock_chat):
        """Test that generate_text works with various prompts."""
        mock_chat.return_value = {
            'message': {
                'content': 'Response content'
            }
        }
        
        prompts = [
            'Simple question',
            'Multi\nline\nprompt',
            'Prompt with special chars: !@#$%^&*()',
            '',  # Empty prompt
        ]
        
        for prompt in prompts:
            result = generate_text(prompt)
            assert result == 'Response content'

    @patch('gitgenie.llm_client.ollama.chat')
    def test_generate_text_handles_connection_error(self, mock_chat):
        """Test that generate_text returns None on connection error."""
        mock_chat.side_effect = ConnectionError('Cannot connect to Ollama')
        
        result = generate_text('Test prompt')
        
        assert result is None

    @patch('gitgenie.llm_client.ollama.chat')
    def test_generate_text_handles_timeout_error(self, mock_chat):
        """Test that generate_text returns None on timeout."""
        mock_chat.side_effect = TimeoutError('Request timed out')
        
        result = generate_text('Test prompt')
        
        assert result is None

    @patch('gitgenie.llm_client.ollama.chat')
    def test_generate_text_handles_generic_exception(self, mock_chat):
        """Test that generate_text returns None on any exception."""
        mock_chat.side_effect = Exception('Unknown error')
        
        result = generate_text('Test prompt')
        
        assert result is None

    @patch('gitgenie.llm_client.ollama.chat')
    def test_generate_text_handles_key_error(self, mock_chat):
        """Test that generate_text returns None if response format is unexpected."""
        # Mock a malformed response
        mock_chat.return_value = {'wrong_key': 'value'}
        
        result = generate_text('Test prompt')
        
        assert result is None

    @patch('gitgenie.llm_client.ollama.chat')
    def test_generate_text_handles_empty_response(self, mock_chat):
        """Test that generate_text handles empty content in response."""
        mock_chat.return_value = {
            'message': {
                'content': ''
            }
        }
        
        result = generate_text('Test prompt')
        
        assert result == ''

    @patch('gitgenie.llm_client.ollama.chat')
    def test_generate_text_uses_correct_model(self, mock_chat):
        """Test that generate_text uses the llama3 model."""
        mock_chat.return_value = {
            'message': {
                'content': 'Response'
            }
        }
        
        generate_text('Test')
        
        # Verify the model parameter
        call_args = mock_chat.call_args
        assert call_args[1]['model'] == 'llama3'

    @patch('gitgenie.llm_client.ollama.chat')
    def test_generate_text_formats_messages_correctly(self, mock_chat):
        """Test that generate_text formats messages in the correct structure."""
        mock_chat.return_value = {
            'message': {
                'content': 'Response'
            }
        }
        
        prompt = 'Tell me a story'
        generate_text(prompt)
        
        # Verify message structure
        call_args = mock_chat.call_args
        messages = call_args[1]['messages']
        assert len(messages) == 1
        assert messages[0]['role'] == 'user'
        assert messages[0]['content'] == prompt

    @patch('gitgenie.llm_client.ollama.chat')
    def test_generate_text_with_long_prompt(self, mock_chat):
        """Test that generate_text handles long prompts."""
        mock_chat.return_value = {
            'message': {
                'content': 'Response to long prompt'
            }
        }
        
        long_prompt = 'a' * 10000  # Very long prompt
        result = generate_text(long_prompt)
        
        assert result == 'Response to long prompt'
        call_args = mock_chat.call_args
        assert call_args[1]['messages'][0]['content'] == long_prompt