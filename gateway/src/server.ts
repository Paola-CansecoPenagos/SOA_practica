import express from 'express';
import morgan from 'morgan';
import dotenv from 'dotenv';
import { Signale } from 'signale';
import proxy from 'express-http-proxy';

dotenv.config();

const app = express();
const signale = new Signale();
const PORT = process.env.PORT || 8080;

app.use(express.json());
app.use(morgan('dev'));

app.use('/api/inventory', proxy(process.env.INVENTORY_SERVICE_URL || 'http://localhost:8081'));
app.use('/api/orders', proxy(process.env.ORDER_SERVICE_URL || 'http://localhost:8082'));

app.listen(PORT, () => {
  signale.success(`API Gateway running on http://localhost:${PORT}`);
});
