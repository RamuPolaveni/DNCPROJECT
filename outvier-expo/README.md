# Outvier Mobile App

A comprehensive personal growth and team matching mobile application built with React Native and Expo for the Digital Nomad Council (DNC) community.

## 📱 Overview

Outvier is a cross-platform mobile application that empowers users to manage personal development goals, find compatible team members, and track learning progress. The app provides an intuitive interface for digital nomads and remote workers to connect, collaborate, and grow together.

## ✨ Features

### 🎯 Personal Goal Management
- Create, edit, and track personal development goals
- Set priorities, target dates, and progress tracking
- Goal categorization and status management
- Visual progress indicators and completion tracking
- Goal sharing and collaboration features

### 👥 Team Matching System
- AI-powered compatibility matching algorithm
- Find potential collaborators and study partners
- View detailed profiles and compatibility scores
- Accept or decline match requests
- Match history and analytics

### 📚 Learning Pathways
- Browse structured learning curricula
- Enroll in skill development pathways
- Track progress through pathway steps
- Personalized recommendations based on goals
- Completion tracking and achievements

### 📊 Analytics Dashboard
- Progress overview with visual charts
- Learning pattern analysis
- Achievement tracking and insights
- Performance metrics and recommendations
- Real-time data visualization

### 🔐 Secure Authentication
- JWT-based authentication system
- Secure user registration and login
- Session management with token refresh
- Profile management and customization
- Password reset functionality

### 🔔 Notification System
- Real-time push notifications
- In-app notification management
- Notification preferences and settings
- Automated reminder system
- Goal and pathway reminders

## 🛠️ Technology Stack

### Frontend
- **React Native** 0.79.6 - Cross-platform mobile development
- **Expo SDK** 53 - Development platform and tools
- **TypeScript** - Type-safe development
- **React Navigation** v7 - Navigation system
- **TanStack Query** - Data fetching and caching
- **React Native Paper** - Material Design components

### State Management
- **React Context API** - Global state management
- **AsyncStorage** - Local data persistence
- **React Hook Form** - Form handling and validation

### UI/UX
- **React Native Paper** - Material Design components
- **React Native Vector Icons** - Icon library
- **React Native Animatable** - Smooth animations
- **React Native Linear Gradient** - Gradient backgrounds
- **React Native Chart Kit** - Data visualization

### Development Tools
- **Expo CLI** - Development and build tools
- **TypeScript** - Type checking and IntelliSense
- **ESLint** - Code linting and formatting
- **Prettier** - Code formatting

## 🚀 Getting Started

### Prerequisites

- **Node.js** 18.0 or higher
- **npm** or **yarn** package manager
- **Expo CLI** (`npm install -g @expo/cli`)
- **Expo Go** app on your mobile device (for testing)

### Installation

1. **Clone the repository**
   ```bash
   git clone <repository-url>
   cd outvier-expo
   ```

2. **Install dependencies**
   ```bash
   npm install
   # or
   yarn install
   ```

3. **Start the development server**
   ```bash
   npm start
   # or
   yarn start
   ```

4. **Run on device/simulator**
   ```bash
   # For Android
   npm run android
   
   # For iOS
   npm run ios
   
   # For web (development only)
   npm run web
   ```

### Development Setup

1. **Install Expo CLI globally**
   ```bash
   npm install -g @expo/cli
   ```

2. **Install Expo Go on your device**
   - [Android](https://play.google.com/store/apps/details?id=host.exp.exponent)
   - [iOS](https://apps.apple.com/app/expo-go/id982107779)

3. **Start development server**
   ```bash
   expo start
   ```

4. **Scan QR code** with Expo Go app to run on your device

## 📱 App Structure

```
src/
├── components/          # Reusable UI components
│   ├── LoadingScreen.tsx
│   ├── ErrorScreen.tsx
│   ├── GoalCard.tsx
│   ├── MatchCard.tsx
│   ├── ProgressCard.tsx
│   ├── SearchBar.tsx
│   ├── FilterModal.tsx
│   ├── CustomButton.tsx
│   ├── CustomInput.tsx
│   └── FullscreenToggle.tsx
├── contexts/           # Global state management
│   ├── AuthContext.tsx
│   ├── ThemeContext.tsx
│   └── FullscreenContext.tsx
├── navigation/         # Navigation configuration
│   ├── AppNavigator.tsx
│   └── AuthNavigator.tsx
├── screens/           # App screens
│   ├── auth/
│   │   ├── LoginScreen.tsx
│   │   └── RegisterScreen.tsx
│   ├── dashboard/
│   │   ├── DashboardScreen.tsx
│   │   ├── AnalyticsScreen.tsx
│   │   ├── ProfileSettingsScreen.tsx
│   │   ├── NotificationsScreen.tsx
│   │   └── AchievementsScreen.tsx
│   ├── goals/
│   │   ├── GoalsScreen.tsx
│   │   ├── EnhancedGoal.tsx
│   │   ├── GoalDetailScreen.tsx
│   │   └── CreateGoalScreen.tsx
│   ├── matches/
│   │   ├── MatchesScreen.tsx
│   │   └── MatchDetailScreen.tsx
│   ├── pathways/
│   │   ├── PathwaysScreen.tsx
│   │   ├── PathwayDetailScreen.tsx
│   │   └── LearningProcessScreen.tsx
│   └── profile/
│       └── ProfileScreen.tsx
├── services/          # API and external services
│   └── api.ts
├── styles/           # Styling and themes
│   ├── theme.ts
│   ├── colors.ts
│   ├── typography.ts
│   └── mobileLayout.ts
├── types/            # TypeScript type definitions
│   ├── auth.ts
│   ├── goals.ts
│   ├── matches.ts
│   ├── pathways.ts
│   └── common.ts
└── utils/            # Utility functions
    ├── storage.ts
    ├── validation.ts
    └── helpers.ts
```

## 🎨 Design System

### Color Palette
- **Primary**: #6366F1 (Indigo)
- **Secondary**: #8B5CF6 (Purple)
- **Success**: #10B981 (Emerald)
- **Warning**: #F59E0B (Amber)
- **Error**: #EF4444 (Red)
- **Background**: #F8FAFC (Slate)
- **Surface**: #FFFFFF (White)

### Typography
- **Headings**: Inter Bold
- **Body**: Inter Regular
- **Captions**: Inter Medium

### Components
- **Cards**: Rounded corners, subtle shadows
- **Buttons**: Material Design principles
- **Inputs**: Clear labels, error states
- **Navigation**: Bottom tabs with icons

## 📊 Key Features Implementation

### Authentication Flow
```typescript
// JWT-based authentication with secure storage
const { user, login, logout, isLoading } = useAuth();

// Automatic token refresh
useEffect(() => {
  const refreshToken = async () => {
    // Token refresh logic
  };
}, []);
```

### Goal Management
```typescript
// Create and manage personal goals
const createGoal = async (goalData: CreateGoalData) => {
  const response = await api.post('/outvier/goals/', goalData);
  return response.data;
};

// Track goal progress
const updateGoalProgress = async (goalId: string, progress: number) => {
  const response = await api.patch(`/outvier/goals/${goalId}/`, { progress });
  return response.data;
};
```

### Team Matching
```typescript
// Find compatible team members
const findMatches = async () => {
  const response = await api.post('/outvier/matches/find/');
  return response.data;
};

// Accept or reject matches
const handleMatchAction = async (matchId: string, action: 'accept' | 'reject') => {
  const response = await api.post(`/outvier/matches/${matchId}/${action}/`);
  return response.data;
};
```

### Learning Pathways
```typescript
// Enroll in learning pathways
const enrollInPathway = async (pathwayId: string) => {
  const response = await api.post(`/outvier/pathways/${pathwayId}/enroll/`);
  return response.data;
};

// Complete pathway steps
const completeStep = async (pathwayId: string, stepId: string) => {
  const response = await api.post(`/outvier/pathways/${pathwayId}/complete-step/`, { step_id: stepId });
  return response.data;
};
```

### Analytics Dashboard
```typescript
// Fetch analytics data
const { data: analyticsData } = useQuery({
  queryKey: ['analytics'],
  queryFn: async () => {
    const response = await api.get('/outvier/dashboard/analytics/');
    return response.data;
  },
});
```

## 🔧 Configuration

### Environment Variables
Create a `.env` file in the root directory:

```env
# API Configuration
API_BASE_URL=http://192.168.13.174:8000/api
API_TIMEOUT=10000

# App Configuration
APP_NAME=Outvier
APP_VERSION=1.0.0

# Feature Flags
ENABLE_FULLSCREEN_MODE=true
ENABLE_ANALYTICS=true
ENABLE_NOTIFICATIONS=true
```

### API Integration
The app connects to a Django REST Framework backend. Update the API base URL in `src/services/api.ts`:

```typescript
const API_BASE_URL = process.env.API_BASE_URL || 'http://192.168.13.174:8000/api';
```

## 📱 Platform Support

### Android
- **Minimum**: Android 7.0 (API level 24)
- **Recommended**: Android 11+ with 6GB+ RAM
- **Features**: Full feature support including fullscreen mode

### iOS
- **Minimum**: iOS 12.0
- **Recommended**: iOS 15+ with 4GB+ RAM
- **Features**: Complete compatibility with native feel

### Web (Development)
- **Browser**: Chrome, Firefox, Safari, Edge
- **Features**: Limited functionality for development testing

## 🚀 Building for Production

### Android APK
```bash
# Build Android APK
expo build:android

# Or use EAS Build
eas build --platform android
```

### iOS IPA
```bash
# Build iOS IPA
expo build:ios

# Or use EAS Build
eas build --platform ios
```

### Web Build
```bash
# Build for web
expo build:web
```

## 🧪 Testing

### Running Tests
```bash
# Run all tests
npm test

# Run tests in watch mode
npm run test:watch

# Run tests with coverage
npm run test:coverage
```

### Testing on Devices
1. **Physical Device**: Use Expo Go app
2. **Android Emulator**: Android Studio AVD
3. **iOS Simulator**: Xcode Simulator

## 📦 Dependencies

### Core Dependencies
- `expo` - Expo SDK
- `react` - React library
- `react-native` - React Native framework
- `@react-navigation/native` - Navigation
- `@tanstack/react-query` - Data fetching
- `react-native-paper` - UI components

### Development Dependencies
- `typescript` - Type checking
- `@types/react` - React types
- `@babel/core` - Babel compiler

## 🔒 Security Features

- **JWT Authentication**: Secure token-based authentication
- **Secure Storage**: Encrypted local storage for sensitive data
- **Input Validation**: Client-side validation for all forms
- **HTTPS Communication**: Secure API communication
- **Session Management**: Automatic token refresh and logout

## 🎯 Performance Optimizations

- **Lazy Loading**: Components loaded on demand
- **Image Optimization**: Optimized image loading and caching
- **Memory Management**: Efficient state management
- **Bundle Splitting**: Optimized bundle size
- **Caching**: Intelligent data caching with TanStack Query

## 🐛 Troubleshooting

### Common Issues

1. **Metro bundler issues**
   ```bash
   npx expo start --clear
   ```

2. **Dependencies conflicts**
   ```bash
   rm -rf node_modules package-lock.json
   npm install
   ```

3. **Expo CLI issues**
   ```bash
   npm install -g @expo/cli@latest
   ```

4. **Android build issues**
   ```bash
   cd android && ./gradlew clean
   ```

5. **Navigation issues**
   ```bash
   # Clear navigation cache
   npx expo start --clear
   ```

### Debug Mode
Enable debug mode in development:
```typescript
// In App.tsx
if (__DEV__) {
  console.log('Debug mode enabled');
}
```

## 📚 Documentation

- [Expo Documentation](https://docs.expo.dev/)
- [React Native Documentation](https://reactnative.dev/)
- [React Navigation](https://reactnavigation.org/)
- [TanStack Query](https://tanstack.com/query/latest)
- [React Native Paper](https://reactnativepaper.com/)

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🆘 Support

For support and questions:
- Create an issue in the repository
- Check the documentation
- Contact the development team

## 🎉 Acknowledgments

- Digital Nomad Council community
- React Native and Expo teams
- Open source contributors
- Material Design team

---

**Version**: 1.0.0  
**Last Updated**: January 2025  
**Platform**: React Native with Expo  
**Target**: Android & iOS