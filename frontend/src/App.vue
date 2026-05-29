<script setup>
import { ref, reactive, computed, onMounted, onBeforeUnmount } from 'vue'
import chiikawaImg from './assets/Chiikawa emoji.png'
import usagiImg from './assets/usagi emoji.png'
import hachiwareImg from './assets/Hachiware emoji.png'
import kaniImg from './assets/Kani emoji.png'
import momongaImg from './assets/momonga emoji.png'
import rakkoImg from './assets/Rakko emoji.png'

const playing = ref(false)
const score = ref(0)
const timeLeft = ref(20)
const hits = ref(0)
const message = ref('Tap a Chiikawa to score!')
const highscore = reactive({ score: 0, player: 'Chiikawa' })
const badgeChars = [chiikawaImg, usagiImg, hachiwareImg]
const characterImages = [chiikawaImg, usagiImg, hachiwareImg, kaniImg, momongaImg, rakkoImg]
const target = reactive({ x: 50, y: 50, src: chiikawaImg, label: 'Chiikawa' })
let moveInterval = null
let countdownInterval = null

const targetStyle = computed(() => ({
  left: `${target.x}%`,
  top: `${target.y}%`,
  transform: 'translate(-50%, -50%)',
}))

function randomizeTarget() {
  const index = Math.floor(Math.random() * characterImages.length)
  target.x = 10 + Math.random() * 80
  target.y = 15 + Math.random() * 70
  target.src = characterImages[index]
  target.label = `Chiikawa ${index + 1}`
}

async function loadHighscore() {
  try {
    const response = await fetch('/api/highscore')
    if (!response.ok) throw new Error('Unable to load high score')
    const data = await response.json()
    highscore.score = data.score ?? 0
    highscore.player = data.player ?? 'Chiikawa'
  } catch {
    highscore.score = 0
    highscore.player = 'Chiikawa'
  }
}

async function submitScore() {
  if (score.value < 1) return
  try {
    const response = await fetch('/api/highscore', {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify({ player: 'You', score: score.value }),
    })
    if (!response.ok) throw new Error('Unable to save score')
    const data = await response.json()
    highscore.score = data.highscore.score
    highscore.player = data.highscore.player
    if (data.status === 'new-highscore') {
      message.value = 'New high score! 🎉'
    }
  } catch {
    message.value = 'Score saved locally. Try again later.'
  }
}

function stopTimers() {
  if (moveInterval) {
    clearInterval(moveInterval)
    moveInterval = null
  }
  if (countdownInterval) {
    clearInterval(countdownInterval)
    countdownInterval = null
  }
}

function endGame() {
  stopTimers()
  playing.value = false
  message.value = score.value > 0 ? 'Game over! Tap Start to play again.' : 'Try to hit the Chiikawa!'
  submitScore()
}

function startGame() {
  score.value = 0
  hits.value = 0
  timeLeft.value = 20
  message.value = 'Find the Chiikawa and click fast!'
  playing.value = true
  randomizeTarget()

  moveInterval = setInterval(randomizeTarget, 900)
  countdownInterval = setInterval(() => {
    timeLeft.value -= 1
    if (timeLeft.value <= 0) {
      endGame()
    }
  }, 1000)
}

function hitTarget() {
  if (!playing.value) return
  score.value += 10
  hits.value += 1
  message.value = ['So cute!', 'Nice hit!', 'Great job!', 'Chiikawa got clicked!'][Math.floor(Math.random() * 4)]
  randomizeTarget()
}

onMounted(() => {
  loadHighscore()
})

onBeforeUnmount(() => {
  stopTimers()
})
</script>

<template>
  <div class="game-shell">
    <header class="hero-panel">
      <div>
        <span class="badge">Chiikawa Clicker</span>
        <div class="emoji-strip">
          <img v-for="(icon, index) in badgeChars" :key="index" :src="icon" alt="Badge icon" />
        </div>
        <h1>Tap the cute Chiikawa before time runs out</h1>
        <p>Vue + FastAPI full-stack game with a backend high score tracker.</p>
      </div>
      <div class="score-banner">
        <span>High score</span>
        <strong>{{ highscore.score }}</strong>
        <small>by {{ highscore.player }}</small>
      </div>
    </header>

    <section class="info-grid">
      <article>
        <span>Score</span>
        <strong>{{ score }}</strong>
      </article>
      <article>
        <span>Time</span>
        <strong>{{ timeLeft }}</strong>
      </article>
      <article>
        <span>Hits</span>
        <strong>{{ hits }}</strong>
      </article>
      <article>
        <span>Status</span>
        <strong>{{ message }}</strong>
      </article>
    </section>

    <section class="game-area">
      <div class="arena">
        <button type="button" class="target" :style="targetStyle" @click="hitTarget" :aria-label="`Chiikawa target ${target.label}`">
          <img class="target-img" :src="target.src" :alt="target.label" />
        </button>
        <div class="start-card" v-if="!playing">
          <h2>Ready?</h2>
          <p>Score as many hits as you can in 20 seconds.</p>
          <button @click="startGame">Start Game</button>
        </div>
      </div>
    </section>

    <footer class="footer-panel">
      <p>Run <code>cd frontend && npm run dev</code> and <code>cd ../backend && venv\Scripts\python main.py</code> to play locally.</p>
    </footer>
  </div>
</template>
