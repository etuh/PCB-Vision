<template>
    <div class="auth-container">
        <div class="auth-box">
            <h2>Create Account</h2>
            <form @submit.prevent="handleRegister">
                <div class="input-group">
                    <label for="username">Username</label>
                    <input type="text" id="username" v-model="username" placeholder="yourusername" required />
                </div>
                <div class="input-group">
                    <label for="email">Email</label>
                    <input type="email" id="email" v-model="email" placeholder="you@example.com" required />
                </div>
                <div class="input-group">
                    <label for="password">Password</label>
                    <input type="password" id="password" v-model="password" placeholder="••••••••" required />
                </div>
                <div class="input-group">
                    <label for="confirm-password">Confirm Password</label>
                    <input type="password" id="confirm-password" v-model="confirmPassword" placeholder="••••••••"
                        required />
                </div>
                <button type="submit" class="submit-button">Register</button>
            </form>
            <div class="footer">
                <p>
                    Already have an account?
                    <router-link to="/login">Login</router-link>
                </p>
            </div>
        </div>
    </div>
</template>

<script setup>
import { ref } from 'vue';
import { useRouter } from 'vue-router';

const router = useRouter();
const username = ref('');
const email = ref('');
const password = ref('');
const confirmPassword = ref('');

const handleRegister = () => {
    if (password.value !== confirmPassword.value) {
        alert("Passwords do not match!");
        return;
    }
    console.log('Registering with:', username.value, email.value);
    // Add your API call to Django for registration here
    // On success, you might redirect to the login page or a dashboard
    // router.push('/login');
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
    margin-top: 1rem;

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