const sqlite3 = require('sqlite3').verbose();
const path = require('path');
const fs = require('fs');

const dbPath = path.resolve(__dirname, 'database.sqlite');
const db = new sqlite3.Database(dbPath, (err) => {
    if (err) {
        console.error('Could not connect to database', err);
        process.exit(1);
    }
    console.log('Connected to database');
});

const userCount = 200;
const users = [];

// Prepare CSV lists
const searchTerms = [
    { keyword: 'iPhone' },
    { keyword: 'Samsung' },
    { keyword: 'MacBook' },
    { keyword: 'AirPods' },
    { keyword: 'Keychron' },
    { keyword: 'Điện thoại' },
    { keyword: 'Laptop' },
    { keyword: 'Phụ kiện' }
];

const checkoutData = [
    { address: '123 Le Loi, TP.HCM', quantity: 1 },
    { address: '456 Nguyen Hue, TP.HCM', quantity: 2 },
    { address: '789 Tran Hung Dao, TP.HCM', quantity: 1 },
    { address: '101 CMT8, TP.HCM', quantity: 3 },
    { address: '202 Nguyen Trai, TP.HCM', quantity: 1 },
    { address: '303 Le Hong Phong, TP.HCM', quantity: 2 }
];

db.serialize(() => {
    // Insert 200 users into DB (ignoring errors if user already exists, or deleting them first)
    // To ensure clean slate, we can just delete users whose email matches 'user*@eshop.com'
    db.run("DELETE FROM users WHERE email LIKE 'user%@eshop.com'", (err) => {
        if (err) console.error(err);
    });

    const stmt = db.prepare("INSERT INTO users (name, email, password, role) VALUES (?, ?, ?, 'user')");
    for (let i = 1; i <= userCount; i++) {
        const email = `user${i}@eshop.com`;
        const password = 'Password123!';
        const name = `Performance User ${i}`;
        stmt.run(name, email, password);
        users.push({ email, password });
    }
    stmt.finalize((err) => {
        if (err) {
            console.error('Error finalising user insertion:', err);
        } else {
            console.log(`Successfully seeded ${userCount} users into SQLite database.`);
            writeCsvFiles();
        }
        db.close();
    });
});

function writeCsvFiles() {
    // Write CSV files in the workspace root (one level up from backend)
    const targetDir = path.resolve(__dirname, '..');

    // 1. Write users.csv
    const usersCsvContent = 'email,password\n' + users.map(u => `${u.email},${u.password}`).join('\n');
    fs.writeFileSync(path.resolve(targetDir, 'users.csv'), usersCsvContent);
    console.log('Created users.csv at', path.resolve(targetDir, 'users.csv'));

    // 2. Write search_terms.csv
    const searchCsvContent = 'keyword\n' + searchTerms.map(s => `${s.keyword}`).join('\n');
    fs.writeFileSync(path.resolve(targetDir, 'search_terms.csv'), searchCsvContent);
    console.log('Created search_terms.csv at', path.resolve(targetDir, 'search_terms.csv'));

    // 3. Write checkout_data.csv
    const checkoutCsvContent = 'address,quantity\n' + checkoutData.map(c => `"${c.address}",${c.quantity}`).join('\n');
    fs.writeFileSync(path.resolve(targetDir, 'checkout_data.csv'), checkoutCsvContent);
    console.log('Created checkout_data.csv at', path.resolve(targetDir, 'checkout_data.csv'));
}
