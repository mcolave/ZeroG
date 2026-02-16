document.addEventListener('DOMContentLoaded', () => {
    // --- Elements ---
    const micBtn = document.getElementById('mic-btn');
    const cameraBtn = document.getElementById('camera-btn');
    const sendBtn = document.getElementById('send-btn');
    const foodInput = document.getElementById('food-input');
    const fileUpload = document.getElementById('file-upload');
    const voiceStatus = document.getElementById('voice-status');
    const settingsBtn = document.getElementById('settings-btn');
    const closeSettingsBtn = document.getElementById('close-settings');
    const settingsModal = document.getElementById('settings-modal');
    const diabetesToggle = document.getElementById('diabetes-toggle');
    const ckdToggle = document.getElementById('ckd-toggle');

    // Add Food Elements
    const addFoodModal = document.getElementById('add-food-modal');
    const closeAddFoodBtn = document.getElementById('close-add-food');
    const saveFoodBtn = document.getElementById('save-food-btn');
    const newFoodName = document.getElementById('new-food-name');
    const newCarbs = document.getElementById('new-carbs');
    const newFats = document.getElementById('new-fats');
    const newProtein = document.getElementById('new-protein');
    const newCalories = document.getElementById('new-calories');

    // --- State ---
    let isRecording = false;

    // Data from user request
    const PRESETS = {
        '1000': { cal: 1000, carbs: 128, prot: 45, fat: 37 },
        '1100': { cal: 1100, carbs: 140, prot: 50, fat: 40 },
        '1200': { cal: 1200, carbs: 153, prot: 54, fat: 44 },
        '1300': { cal: 1300, carbs: 166, prot: 59, fat: 48 },
        '1400': { cal: 1400, carbs: 179, prot: 63, fat: 51 },
        '1500': { cal: 1500, carbs: 191, prot: 68, fat: 55 },
        '1600': { cal: 1600, carbs: 204, prot: 72, fat: 59 },
        '1700': { cal: 1700, carbs: 217, prot: 77, fat: 62 },
        '1800': { cal: 1800, carbs: 230, prot: 81, fat: 66 },
        '1900': { cal: 1900, carbs: 242, prot: 86, fat: 70 },
        '2000': { cal: 2000, carbs: 255, prot: 90, fat: 73 },
        '2100': { cal: 2100, carbs: 268, prot: 95, fat: 77 },
        '2200': { cal: 2200, carbs: 281, prot: 99, fat: 81 },
        '2300': { cal: 2300, carbs: 293, prot: 104, fat: 84 },
        '2400': { cal: 2400, carbs: 306, prot: 108, fat: 88 },
        '2500': { cal: 2500, carbs: 319, prot: 113, fat: 92 },
    };

    // --- Initialization ---
    fetchData();

    // --- Event Listeners ---

    // Voice Input
    if ('webkitSpeechRecognition' in window) {
        const recognition = new webkitSpeechRecognition();
        recognition.continuous = false;
        recognition.interimResults = false;
        recognition.lang = 'en-US';

        micBtn.addEventListener('click', () => {
            if (isRecording) {
                recognition.stop();
            } else {
                recognition.start();
            }
        });

        recognition.onstart = () => {
            isRecording = true;
            micBtn.classList.add('recording');
            voiceStatus.classList.remove('hidden');
            voiceStatus.innerText = "Listening...";
        };

        recognition.onend = () => {
            isRecording = false;
            micBtn.classList.remove('recording');
            voiceStatus.classList.add('hidden');
        };

        recognition.onresult = (event) => {
            const transcript = event.results[0][0].transcript;
            foodInput.value = transcript;
        };
    } else {
        micBtn.style.display = 'none'; // Hide if not supported
        console.log("Web Speech API not supported");
    }

    // Image Upload (Trigger hidden input)
    cameraBtn.addEventListener('click', () => {
        fileUpload.click();
    });

    fileUpload.addEventListener('change', (e) => {
        if (e.target.files.length > 0) {
            alert("Image selected! (Image processing would happen here)");
            // In a real app, upload via FormData to /api/upload
        }
    });

    // Send Input
    sendBtn.addEventListener('click', submitLog);
    foodInput.addEventListener('keypress', (e) => {
        if (e.key === 'Enter') submitLog();
    });

    // Settings Modal
    settingsBtn.addEventListener('click', () => settingsModal.classList.remove('hidden'));
    closeSettingsBtn.addEventListener('click', () => settingsModal.classList.add('hidden'));

    settingsModal.addEventListener('click', (e) => {
        if (e.target === settingsModal) settingsModal.classList.add('hidden');
    });

    // Settings Toggles
    diabetesToggle.addEventListener('change', updateSettings);
    ckdToggle.addEventListener('change', updateSettings);

    // Add Food Modal Logic
    if (closeAddFoodBtn) {
        closeAddFoodBtn.addEventListener('click', () => addFoodModal.classList.add('hidden'));
    }

    if (saveFoodBtn) {
        saveFoodBtn.addEventListener('click', async () => {
            const name = newFoodName.value.trim();
            if (!name) return;

            const foodData = {
                name: name,
                carbs: parseFloat(newCarbs.value) || 0,
                fats: parseFloat(newFats.value) || 0,
                protein: parseFloat(newProtein.value) || 0,
                calories: parseFloat(newCalories.value) || 0
            };

            try {
                // Change button state
                const originalText = saveFoodBtn.innerText;
                saveFoodBtn.innerText = 'Saving...';

                const response = await fetch('/api/add_food', {
                    method: 'POST',
                    headers: { 'Content-Type': 'application/json' },
                    body: JSON.stringify(foodData)
                });

                if ((await response.json()).status === 'success') {
                    addFoodModal.classList.add('hidden');
                    // Retry logging
                    submitLog();
                }
                saveFoodBtn.innerText = originalText;
            } catch (error) {
                console.error("Error saving food:", error);
            }
        });
    }

    // --- Functions ---

    // Nutrition Popup Elements
    const nutritionPopup = document.getElementById('nutrition-popup');
    const closeNutritionPopupBtn = document.getElementById('close-nutrition-popup');
    const popupName = document.getElementById('popup-food-name');
    const popupCal = document.getElementById('popup-cal');
    const popupCarbs = document.getElementById('popup-carbs');
    const popupProt = document.getElementById('popup-protein');
    const popupFats = document.getElementById('popup-fats');

    if (closeNutritionPopupBtn) {
        closeNutritionPopupBtn.addEventListener('click', () => nutritionPopup.classList.add('hidden'));
    }

    async function submitLog() {
        // ... (existing pre-logic) ...
        const text = foodInput.value.trim();
        if (!text) return;
        sendBtn.innerHTML = '<i class="fa-solid fa-spinner fa-spin"></i>';

        try {
            const response = await fetch('/api/log', {
                method: 'POST',
                headers: { 'Content-Type': 'application/json' },
                body: JSON.stringify({ text: text })
            });
            const data = await response.json();

            if (data.status === 'success') {
                foodInput.value = ''; // Clear input
                fetchData(); // Refresh stats
            } else if (data.status === 'unknown') {
                // ... (existing add food logic) ...
                let suggestedName = text.replace(/[0-9]+/g, '').replace(/\b(grams|gram|g)\b/gi, '').trim();
                newFoodName.value = suggestedName;
                addFoodModal.classList.remove('hidden');
            }
        } catch (error) {
            console.error("Error logging:", error);
        } finally {
            sendBtn.innerHTML = '<i class="fa-solid fa-paper-plane"></i>';
        }
    }

    async function fetchData() {
        try {
            const response = await fetch('/api/data?t=' + new Date().getTime());
            const data = await response.json();
            // console.log("Fetcher Data:", data); // Debug

            if (data.totals && data.targets) {
                updateDashboard(data.totals, data.targets);
                updateSettingsUI(data.targets);

                // Update History List
                if (data.history) {
                    updateHistoryList(data.history);
                }
            }
        } catch (error) {
            console.error("Error fetching data:", error);
        }
    }

    function updateHistoryList(history) {
        const listEl = document.getElementById('history-list');
        if (!listEl) return;

        if (history.length === 0) {
            listEl.innerHTML = '<div style="text-align: center; color: var(--text-secondary);">No logs yet today.</div>';
            return;
        }

        listEl.innerHTML = '';
        history.forEach(item => {
            const div = document.createElement('div');
            div.className = 'history-item glass-panel';
            div.style.padding = '10px';
            div.style.display = 'flex';
            div.style.justifyContent = 'space-between';
            div.style.alignItems = 'center';
            div.style.background = 'rgba(255,255,255,0.05)';
            div.style.marginBottom = '6px';
            div.style.cursor = 'help'; // Indicate hoverable

            // Add detailed info on hover
            const details = `Calories: ${Math.round(item.calories)}\nCarbs: ${Math.round(item.carbs)}g\nProtein: ${Math.round(item.protein)}g\nFats: ${Math.round(item.fats)}g\nPotassium: ${Math.round(item.potassium)}mg`;
            div.title = details;

            div.innerHTML = `
                <div>
                    <div style="font-weight: bold; text-transform: capitalize;">${item.content || 'Food Entry'}</div>
                    <div style="font-size: 0.8rem; color: var(--text-secondary);">
                        ${Math.round(item.calories)} kcal
                    </div>
                </div>
                <div style="text-align: right; font-size: 0.85rem;">
                    <span style="color: #00d2ff;">${Math.round(item.carbs)}g C</span> • 
                    <span style="color: #9d50bb;">${Math.round(item.protein)}g P</span> • 
                    <span style="color: #3a7bd5;">${Math.round(item.fats)}g F</span>
                </div>
            `;
            listEl.appendChild(div);
        });
    }

    // Calorie Preset Logic
    const caloriePreset = document.getElementById('calorie-preset');
    const targetCal = document.getElementById('target-calories');
    const targetCarbs = document.getElementById('target-carbs');
    const targetProt = document.getElementById('target-protein');
    const targetFats = document.getElementById('target-fats');
    const targetPotas = document.getElementById('target-potassium');
    const saveSettingsBtn = document.getElementById('save-settings-btn');
    const resetBtn = document.getElementById('reset-btn');

    if (caloriePreset) {
        caloriePreset.addEventListener('change', () => {
            const val = caloriePreset.value;
            if (PRESETS[val]) {
                targetCal.value = PRESETS[val].cal;
                targetCarbs.value = PRESETS[val].carbs;
                targetProt.value = PRESETS[val].prot;
                targetFats.value = PRESETS[val].fat;
            }
        });
    }

    if (saveSettingsBtn) {
        saveSettingsBtn.addEventListener('click', updateSettings);
    }

    if (resetBtn) {
        resetBtn.addEventListener('click', async () => {
            if (confirm("Are you sure you want to clear all food logs for today?")) {
                try {
                    resetBtn.innerText = "Clearing...";
                    await fetch('/api/reset', { method: 'POST' });
                    await fetchData();
                    resetBtn.innerText = "Data Cleared";
                    setTimeout(() => resetBtn.innerText = "Reset Today's Data", 2000);
                } catch (error) {
                    console.error("Error resetting:", error);
                    resetBtn.innerText = "Error";
                }
            }
        });
    }
    // Remove auto-update on toggles to prevent confusion, keep 'Save' button as main action for now, 
    // or keep toggles as immediate but inputs need save via button. 
    // Let's make updateSettings handle everything.

    // ... (rest of function) ...

    function updateSettingsUI(settings) {
        diabetesToggle.checked = !!settings.diabetes_mode;
        ckdToggle.checked = !!settings.ckd_mode;

        // Populate inputs
        const currentCal = settings.target_calories || 2000;
        const currentCarbs = settings.target_carbs || 250;
        const currentProt = settings.target_protein || 100;
        const currentFats = settings.target_fats || 70;
        const currentPotas = settings.target_potassium || 3500;

        if (targetCal) targetCal.value = currentCal;
        if (targetCarbs) targetCarbs.value = currentCarbs;
        if (targetProt) targetProt.value = currentProt;
        if (targetFats) targetFats.value = currentFats;
        if (targetPotas) targetPotas.value = currentPotas;

        // Sync Preset Dropdown
        // Check if current values match any preset
        let foundPreset = 'custom';
        for (const [key, preset] of Object.entries(PRESETS)) {
            if (preset.cal === currentCal &&
                preset.carbs === currentCarbs &&
                preset.prot === currentProt &&
                preset.fat === currentFats) {
                foundPreset = key;
                break;
            }
        }
        if (caloriePreset) caloriePreset.value = foundPreset;
    }

    async function updateSettings() {
        // Change button text
        if (saveSettingsBtn) saveSettingsBtn.innerText = "Saving...";

        const newSettings = {
            diabetes_mode: diabetesToggle.checked ? 1 : 0,
            ckd_mode: ckdToggle.checked ? 1 : 0,
            target_calories: parseFloat(targetCal.value) || 2000,
            target_carbs: parseFloat(targetCarbs.value) || 250,
            target_protein: parseFloat(targetProt.value) || 100,
            target_fats: parseFloat(targetFats.value) || 70,
            target_potassium: parseFloat(targetPotas.value) || 3500
        };

        try {
            await fetch('/api/settings', {
                method: 'POST',
                headers: { 'Content-Type': 'application/json' },
                body: JSON.stringify(newSettings)
            });
            await fetchData(); // Refresh dashboard
            if (saveSettingsBtn) saveSettingsBtn.innerText = "Saved!";
            setTimeout(() => { if (saveSettingsBtn) saveSettingsBtn.innerText = "Save Targets"; }, 2000);
        } catch (error) {
            console.error("Error updating settings:", error);
            if (saveSettingsBtn) saveSettingsBtn.innerText = "Error";
        }
    }


    function updateDashboard(totals, targets) {
        // Update Circular Progress Bars
        updateRing('carbs', totals.carbs, targets.target_carbs);
        updateRing('fats', totals.fats, targets.target_fats);
        updateRing('protein', totals.protein, targets.target_protein);

        // Update Monitors (Linear Bars)
        updateBar('potas', totals.potassium, targets.target_potassium);
        updateBar('cal', totals.calories, targets.target_calories);
        updateBar('sodium', totals.sodium, targets.target_sodium || 2300);
        updateBar('sat-fat', totals.saturated_fat, targets.target_saturated_fat || 20);
        updateBar('trans-fat', totals.trans_fat, targets.target_trans_fat || 0);
    }

    function updateRing(stat, used, total) {
        const circle = document.querySelector(`[data-stat="${stat}"] .progress-ring__circle`);
        const usedEl = document.getElementById(`${stat}-used`);
        const leftEl = document.getElementById(`${stat}-left`);
        const totalEl = document.getElementById(`${stat}-total`);

        // Update Text Elements FIRST (Reliability)
        if (usedEl) usedEl.innerText = used.toFixed(0);
        if (totalEl) totalEl.innerText = total.toFixed(0);
        if (leftEl) leftEl.innerText = (total - used).toFixed(0);

        // Update Circle Animation
        if (!circle) return;

        const radius = circle.r.baseVal.value;
        const circumference = radius * 2 * Math.PI;

        circle.style.strokeDasharray = `${circumference} ${circumference}`;

        const percent = Math.min(used / total, 1);
        const offset = circumference - (percent * circumference);

        circle.style.strokeDashoffset = offset;

        // Color Change if over budget
        if (used > total) {
            circle.style.stroke = '#fc4a1a'; // Danger color
        } else {
            // Reset color based on stat (hacky, ideally classes)
            const colors = { 'carbs': '#00d2ff', 'fats': '#3a7bd5', 'protein': '#9d50bb' };
            circle.style.stroke = colors[stat];
        }
    }

    function updateBar(stat, used, total) {
        const bar = document.getElementById(`${stat}-bar`);
        const valEl = document.getElementById(`${stat}-val`);
        const limitEl = document.getElementById(`${stat}-limit`);

        if (!bar) return;

        const percent = Math.min((used / total) * 100, 100);
        bar.style.width = `${percent}%`;

        if (used > total) {
            bar.style.background = 'var(--danger-color)';
        } else {
            bar.style.background = 'linear-gradient(90deg, var(--secondary-color), var(--primary-color))';
        }

        valEl.innerText = used.toFixed(0);
        limitEl.innerText = total.toFixed(0);
    }
});
