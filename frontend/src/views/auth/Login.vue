<template>
    <div class="auth-container">
        <div class="auth-box">
            <h2>Login</h2>
            <form @submit.prevent="handleLogin">
                <div class="input-group">
                    <label for="email">Email</label>
                    <input type="email" id="email" v-model="email" placeholder="you@example.com" required />
                </div>
                <div class="input-group">
                    <label for="password">Password</label>
                    <input type="password" id="password" v-model="password" placeholder="••••••••" required />
                </div>
                <div class="options">
                    <router-link to="/forgot-password" class="forgot-password">Forgot Password?</router-link>
                </div>
                <button type="submit" class="submit-button">Login</button>
            </form>
            <div class="footer">
                <p>
                    Don't have an account?
                    <router-link to="/register">Create one</router-link>
                </p>
            </div>
        </div>
    </div>
</template>

<script setup>
import { ref } from 'vue';
import { useRouter } from 'vue-router';

// Assuming you are using vue-router
const router = useRouter();

const email = ref('');
const password = ref('');

const handleLogin = () => {
    console.log('Attempting login with:', email.value);
    // Add your authentication logic here (e.g., API call to Django)
    // On success, you might navigate to a dashboard:
    // router.push('/dashboard');
};
</script>

<style lang="scss" scoped>
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
    margin-bottom: 1.5rem;
    color: #1f2937;
    font-size: 1.5rem;
    font-weight: 600;
}

.input-group {
    margin-bottom: 1.25rem;
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

.options {
    text-align: right;
    margin-bottom: 1.5rem;
}

.forgot-password {
    font-size: 0.875rem;
    color: #4f46e5;
    text-decoration: none;

    &:hover {
        text-decoration: underline;
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