<template>
    <div class="auth-container">
        <div class="auth-box">
            <h2>Forgot Password</h2>
            <p class="instructions">
                Enter your email address and we will send you a link to reset your password.
            </p>
            <form @submit.prevent="handlePasswordReset">
                <div class="input-group">
                    <label for="email">Email</label>
                    <input type="email" id="email" v-model="email" placeholder="you@example.com" required />
                </div>
                <button type="submit" class="submit-button">Send Reset Link</button>
            </form>
            <div class="footer">
                <p>
                    <router-link to="/login">Back to Login</router-link>
                </p>
            </div>
        </div>
    </div>
</template>

<script setup>
import { ref } from 'vue';
import { useRouter } from 'vue-router';

const router = useRouter();
const email = ref('');

const handlePasswordReset = () => {
    console.log('Password reset requested for:', email.value);
    // Add your API call logic here to send a password reset email
    // After submitting, you might want to show a confirmation message
    // and/or redirect the user.
    alert('If an account with that email exists, a password reset link has been sent.');
    router.push('/login');
};
</script>

<style lang="scss" scoped>
// Reusing styles from Login.vue for consistency
.auth-container {
    display: flex;
    justify-content: center;
    align-items: center;
    min-height: 100vh;
    background-color: #f3f4f6;
}

.auth-box {
    background: white;
    padding: 2.5rem;
    border-radius: 8px;
    box-shadow: 0 10px 15px -3px rgba(0, 0, 0, 0.1), 0 4px 6px -2px rgba(0, 0, 0, 0.05);
    width: 100%;
    max-width: 400px;
    text-align: center;
}

h2 {
    margin-bottom: 1rem;
    color: #1f2937;
    font-size: 1.5rem;
    font-weight: 600;
}

.instructions {
    margin-bottom: 1.5rem;
    color: #6b7280;
    font-size: 0.9rem;
}

.input-group {
    margin-bottom: 1.5rem;
    text-align: left;
}

.input-group label {
    display: block;
    margin-bottom: 0.5rem;
    color: #374151;
    font-weight: 500;
}

.input-group input {
    width: 100%;
    padding: 0.75rem;
    border: 1px solid #d1d5db;
    border-radius: 4px;
    box-sizing: border-box;
    transition: border-color 0.2s;

    &:focus {
        outline: none;
        border-color: #4f46e5;
        box-shadow: 0 0 0 1px #4f46e5;
    }
}

.submit-button {
    width: 100%;
    padding: 0.75rem;
    border: none;
    border-radius: 4px;
    background-color: #4f46e5;
    color: white;
    font-size: 1rem;
    font-weight: 600;
    cursor: pointer;
    transition: background-color 0.2s;

    &:hover {
        background-color: #4338ca;
    }
}

.footer {
    margin-top: 1.5rem;
    font-size: 0.875rem;
    color: #6b7280;

    a {
        color: #4f46e5;
        text-decoration: none;
        font-weight: 500;

        &:hover {
            text-decoration: underline;
        }
    }
}
</style>